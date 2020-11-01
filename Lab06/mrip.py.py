# Author: Remy Brandriff
# CS460: Computer Networks - Fall 2018
# Lab06: Distance-Vector Routing in Mininet

# Summary: Implementation of MRIP (Minimal Routing Information Protocol) to be used with Mininet, as an exercise
#          for exploring the route discovery phase of distance-vector routing.

# Please see README file for instructions

# Pseudocode courtesy of Wikipedia (https://bit.ly/2DyMS0T)


from multiprocessing import Process
import socket
from random import randint
import time
import argparse
import sys


def main():

    # Create parser and get arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=str, help='Config file name')
    parser.add_argument('-i', type=str, help='Host IP address')

    config_file = sys.argv[1]
    client_ip = sys.argv[2]

    # Parse config file to get:
    # a list of hosts and their IP addresses, and a list of the host's one-hop neighbors
    hosts, graph, hostname = parse_config(config_file, client_ip)

    # Create and start host and client threads (I used Processes due to issues with threads successfully running
    # simultaneously)
    host = Process(target=sender, name="sender", args=(client_ip, graph, hosts, hostname))
    client = Process(target=receiver, name="receiver", args=(client_ip, hosts, graph, hostname))

    host.start()
    client.start()

    # Processes join back up
    host.join()
    client.join()


# Parse config file
def parse_config(filename, ip_addr):
    file = open(filename, "r")

    hostname = ""
    hosts = {}
    neighbor_pairs = []
    graph = {}

    # Iterate through file
    for line in file:

        # If this line is an IP address/hostname pair, save them as 'hostname: ip addr' in dictionary
        # so we have a list of which host goes to which IP address
        if line[0] != 'h':
            item = line.strip().split(" ")
            key = item[1]
            ip = item[0]
            hosts[key] = ip

            if item[0] == ip_addr:
                hostname = item[1]

        # If this line is a one-hop-neighbors pair, save the neighbor pair to a list
        if line[0] == 'h':
            item = line.strip().split(" ")
            host_a = item[0]
            host_b = item[1]
            neighbor_pairs.append((host_a, host_b))

    # find the one-hop neighbors for THIS host and add to a dictionary w/ the value of 1 for the edge's weight
    temp = {}

    for pair in neighbor_pairs:
        if pair[0] == hostname:
            temp[pair[1]] = 1
            graph[pair[0]] = temp

    file.close()

    # return the list of hosts and IP addresses, and the host's graph
    return hosts, graph, hostname


# Broadcasts REQUEST MESSAGES on a timer to the host's one-hop neighbors
def sender(client_ip, graph, hosts, hostname):
    filename = hostname + "_mrip.log"
    log_file = open(filename, "a")

    log_file.write("Initiate host thread\n")

    udp_ip = client_ip
    goal_ip = ""
    udp_port = 5353

    # Create our socket for broadcasting
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    log_file.write("Host socket created\n")

    # Format REQUEST MESSAGE --> 'MRIP REQUEST[host ip addr]\n'
    message = "MRIP REQUEST " + udp_ip + "\n"

    # Broadcast REQUEST MESSAGE every 30 sec + R on port 5353, where R is a random number between 0-30
    while True:
        log_file.write("Host socket listening...\n")

        # Runs through the host's one-hop neighbors to get their IP addresses,
        # and send the message to them
        for n in graph:
            for h in graph[n]:
                neighbor = h

                for i in hosts:
                    if (neighbor == i) and (hosts[neighbor] != udp_ip):
                        goal_ip = hosts[neighbor]

                host_socket.sendto(message, (goal_ip, udp_port))
                log_file.write("Sent '" + message + "' to " + str(goal_ip) + "\n")

        # Sleep
        R = randint(0, 30)
        log_file.write("Host thread wait " + str(R + 30) + "\n")
        time.sleep(30 + R)


# Listens for REQUEST and RESPONSE MESSAGES on port 5353
def receiver(ip, hosts, clients_graph, hostname):
    filename = hostname + "_mrip.log"
    log_file = open(filename, "a")

    log_file.write("Initiate client thread\n")

    start = time.time()

    udp_ip = ip
    udp_port = 5353
    length = 0
    num_hops = 0
    key = ''
    sender_ip = ''
    host_ip = ''
    next_hop = ''
    table_version = 1

    # Create our socket for listening & bind to port 5353
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    log_file.write("Client socket created\n")

    client_socket.bind((udp_ip, udp_port))
    log_file.write("Client socket bound to " + str(udp_ip) + ", " + str(udp_port) + "\n")

    # Listen for incoming messages
    while True:
        log_file.write("Client socket listening\n")

        # Get data (message) & address from sending host
        data, addr = client_socket.recvfrom(1024)

        log_file.write("Received message from " + str(addr) + " : " + data + "\n")

        # Once data has been received, parse it and determine what type of message is it
        split_data = data.split(" ")

        # If message doesn't start correctly, kill the program
        # And b/c this is UDP, we don't owe shit in explanation
        if split_data[0] != "MRIP":
            log_file.write("Error: Incorrectly formatted message\n")
            log_file.close()
            sys.exit()

        else:
            # If this is a REQUEST MESSAGE
            if split_data[1] == "REQUEST":
                log_file.write("Message is a REQUEST MESSAGE\n")
                log_file.write("Message: " + data + "\n")

                # Get the requesting host's IP address (the addr we should send back to) & set OUR IP address
                host_ip = split_data[2].strip()
                sender_ip = udp_ip

                # Get the number of records in our graph
                for host in clients_graph:
                    for neighbor in clients_graph[host]:
                        length += 1
                num_rec = length

                # This is a super janky way to get the number of hops and next hop, but it works, leave me alone
                temp = clients_graph[hostname]
                for item in hosts:
                    if hosts[item] == host_ip:
                        key = item

                for host in temp:
                    if host == key:
                        num_hops = temp[host]

                        # Check the number of hops is within guidelines, otherwise kill
                        if num_hops > 16:
                            sys.exit()
                    if host != key:
                        node = host
                        next_hop = hosts[node]

                    # Format ROUTE MESSAGE (response message)
                    # 'MRIP ROUTE [sender_ip][num_rec]\n
                    #       [host_ip][num_hops][next_hop]\n'
                    message = "MRIP ROUTE " + str(sender_ip) + " " + str(num_rec) + "\n" \
                          + str(host_ip) + " " + str(num_hops) + " " + str(next_hop) + "\n"

                    log_file.write("Host's ROUTE MESSAGE: " + message + "\n")

                    # Send ROUTE MESSAGE back to sending host
                    client_socket.sendto(message, (host_ip, 5353))

                    log_file.write("Message sent to " + host_ip + "\n")

            # Otherwise, if this is a RESPONSE MESSAGE
            elif split_data[1] == "ROUTE":
                log_file.write("Message is a ROUTE MESSAGE\n")
                #log_file.write("Message: " + data)

                # get first part of message and the rest of message (the routing table)
                temp = data.split(" ")
                first = temp[:4]
                table = temp[4:]

                sender_ip = first[2]
                num_rec = first[3]

                temp_v = sender_ip
                for i in hosts:
                    if hosts[i] == temp_v:
                        next_hop = i
                print("Next hop: " + str(next_hop))

                d, p = bellman_ford(clients_graph, next_hop)
                print("Got passed bellman ford")
                table_version += 1
                end = time.time()
                timestamp = end - start

                # Create message to append to log file
                msg = "New Table\n" + "============\nTable Version: " + str(table_version) + "\nTimestamp: " + str(
                    timestamp) + "\nd = " + str(d) + "\np = " + str(p) + "\n"

                log_file = open(filename, "a")

                log_file.write(msg)

            # Otherwise, this message is formatted incorrectly and we kill the program
            else:
                sys.exit()
        # log_file.close()


# Run the Bellman-Ford algorithm
def bellman_ford(vertices, source):

    # Step 1: Initialize graph
    # Pseudocode:
    #            for each vertex v in vertices:
    #               distance[v] := inf
    #               predecessor[v] := null
    #            distance[source[ := 0

    distance = {}
    predecessor = {}

    for v in vertices:
        distance[v] = float('Inf')
        predecessor[v] = None

    distance[source] = 0

    # Step 2: Relax edges

    # Pseudocode:
    #           for i from 1 to size(vertices)-1:
    #               for each edge(u,v) with weight w in edges:
    #                   if distance[u] + w < distance[v]:
    #                       distance[v] := distance[u] + w
    #                       predecessor[v] := u

    for i in range(len(vertices)-1):
        for u in vertices:
            for v in vertices[u]:
                if distance[v] > (distance[u] + vertices[u][v]):

                    distance[v] = distance[u] + vertices[u][v]
                    predecessor[v] = u

    # Step 3: Check for negative-weight cycles

    # Pseudocode:
    #           for each edge(u,v) with weight w in edges:
    #               if distance[u] + (w < distance[v]):
    #                   error("Graph contains a negative weight cycle")
    #           return distance, predecessor

    for u in vertices:
        for v in vertices[u]:
            if distance[u] < (distance[v] + vertices[u][v]):
                sys.exit()

    return distance, predecessor


if __name__ == '__main__':
    main()
