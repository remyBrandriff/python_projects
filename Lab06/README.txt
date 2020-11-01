Author: Remy Brandriff

For CS460 (Computer Networks) - Dr. Morgan Vigil-Hayes - Fall 2018

12 November 2018 -> extended to 21 November 2018


######### Lab06 - Distance-Vector Routing in Mininet ###############################

################################# ABOUT ############################################

This is an implementation of MRIP (Minimal Routing Information Protocol) to be used
with Mininet, as an exercise for exploring the route discovery phase of distance-vector
routing.

When run on hosts in a Mininet topology, the program will use the Bellman-Ford algorithm
to correctly create updated routing tables and cause convergence.

MRIP only implements a
simplified route discovery portion of distance-vector routing.

It uses the following standards.


	1) MRIP must be implemented over UDP


	2) It uses two types of messages: REQUEST and ROUTE


3) It must use port 5353 as a standard port number for REQUEST MESSAGES


	4) It may use a different port for RESPONSE messages


5) The nodes must be pre-configured with routes and costs to their one-hop neighbors


	6) The cost to a one-hop neighbor is calculated by the number of switches between nodes


	7) Nodes only pay attention to its one-hop neighbors


	8) Route discovery must proceed according to the following sequence:

		1. A host requests a table update every 30 seconds + R,
		   where R is a randomly generated number of seconds between 0-30 seconds

		2. When a REQUEST MESSAGE is received, the host sends a ROUTE MESSAGE
		   in response to the requesting host

		3. All hosts should be listening on port 5353

		4. When a ROUTE MESSAGE is received, the host uses the Bellman-Ford
		   algorithm to resolve its routing table


	9) The max hop count is 16. A hop count of 17 indicates an unknown number of hops/infinite number of hops



REQUEST MESSAGES are formatted as follows:


'MRIP REQUEST [sender's IP address]\n'



ROUTE MESSAGES are formatted as follows:


'MRIP ROUTE [sender's IP address][number of records in sender's routing table]\n

	[host's IP address][number of hops from the responder to the host][IP address of next host in the route]\n'



#####################################################################################



The program follows the following outline:



main():


    Gets parameters from command line

    Parses config file

    Starts host thread

    Starts client thread

		Host thread joins

		Client thread joins

parse_config( config filename, client's ip address ):


    The config file is opened and parsed to get the client's hostname and one-hop neighbors

sender( client IP address, graph, hosts, hostname ):

		A client socket is created

		The client sends out REQUEST MESSAGES to its one-hop neighbors every 30+R seconds

receiver( host's IP address, hosts, graph, hostname ):

    A server socket is created


    The client listens for connections


    When a connection is made, it reads in the data

        If the data is a REQUEST MESSAGE:

            The client generates a ROUTE MESSAGE and sends it back


        If the data is a ROUTE MESSAGE:

            The client takes the data in the ROUTE MESSAGE and runs bellman_ford()

            The client resolves its routing table and writes to the log file


        If the data is malformed:

            The program is terminated



bellman_ford( vertices, source node ):

    Uses the Bellman-Ford algorithm to resolve the routing tables


    Step 1: Initialize graph

    Step 2: Relax edges

    Step 3: Check for negative-weight cycles



########## CONFIGURATION FILE ######################################################



The program uses a config file (with the naming format [filename].cnf) to set up the hosts and graph,
to be used in conjunction with Mininet topologies.


Please make sure your config file is formatted as follows:


[Host 1 IP address] [Host 1 name]

[Host 2 IP address] [Host 2 name]

...

[Host X IP address] [Host X name]

[Host 1] [Host 1's one-hop neighbor]

[Host X] [Host X's one-hop neighbor]



EXAMPLE:

10.0.0.1 h1

10.0.0.2 h2

10.0.0.3 h3

h1 h2

h2 h1

h2 h3

h3 h2

Please note that the topology and config file must match; the topology and config files
for ring, mesh, and star+bus topologies have been included with the program.




######### HOW TO RUN ###############################################################



This program was written in Python, and requires at least Python 2.7 to be installed on the machine.

To run it, set up the topology to be used, and use the following command in the Mininet CLI:

python mrip.py [config file name] [host's ip address]



EXAMPLE: python mrip.py config.cnf 10.0.0.1



Run the program on all hosts in the topology. The program will generate log files for
each host with the file name [hostname_mrip.log]. The log files will record REQUEST and ROUTE MESSAGES,
as well as the following information with a timestamp:


[table version]\n
[host's IP address][number of hops][next hop]\n



It may take a while for the routing tables to converge. Once it does, the convergence will
be reflected in the log file; monitor it for changes. If none of the logs have changed
in 2 minutes, you have hit route stability.
