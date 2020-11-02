#!/usr/bin/env python3

# We can use the libraries included here, not just the ones outlined in lab assignment
import argparse
import sys
import itertools
import socket
from socket import socket as Socket

# A simple web server

# Issues:
# Ignores CRLF requirement
# Header must be < 1024 bytes
# ...
# probably loads more

# CS460_TODO is where we need to put a call to the socket api

def main():

    # Command line arguments. Use a port > 1024 by default so that we can run
    # without sudo, for use as a real server you need to use port 80.
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=2080, type=int,
                        help='Port to use')
    args = parser.parse_args()

    # Create the server socket (to handle tcp requests using ipv4), make sure

    # it is always closed by using with statement
    with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: # 1. SOCKET IS OPENED

        # The socket stays connected even after this script ends. So in order
        # to allow the immediate reuse of the socket (so that we can kill and
        # re-run the server while debugging) we set the following option. This
        # is potentially dangerous in real code: in rare cases you may get junk
        # data arriving at the socket.
        
        # Set socket options -- there are  specific option we can pass to the socket to do what we want
        # 2. we can reuse the socket immediately upon close
        # Not in typical use, this is bad form, just b/c we're doing this for class
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind socket to port
        # 3. Just binds socket to the port indicated from the command line or the default we set above
        # blank argument = binding to ourselves and creating a new socket
        # port is hardcoded for now, FIX LATER with strings, right now the socket works
        server_socket.bind(('', 2080))
        
        # 4. Have socket listen, is there an option for this in the socket api?
        # if we leave it blank, it defaults to 0, meaning we can only handle one at a time
        server_socket.listen(0)

        #debugging
        print("server ready")

        # will always run until we close it
        while True:

            # Use the server socket as the connection socket and accept incoming requests
            # This is like file IO and you need to open the server socket as the connection socket

            # 5. accept incoming requests
            # "spawns off multiple server endpoints" - V.H.
            # connection, address; conn_socket is one of those endpoints (connection)
            with server_socket.accept()[0] as conn_socket:

                # Save the request received from the connection and decode as ascii
                # 6. Receive data on the socket (using 1024 as the default buffer size)
                # 7. decode data to ascii
                data_str = conn_socket.recv(1024).decode('ascii')
                print("Got data string\n")
                print(data_str)
                sys.exit(1)

#                 # Generate a reply by sending the request received to http_handle()
#                 # NOT A SOCKET CALL, this will be a call to a subroutine
#                 CS460_TODO
#
#             # Use the connection socket to send the reply encoded as ascii
#             # send reply (encoded as http string/stream??), it's encoded as ascii, we need to encode it as a byte stream
#             CS460_TODO
#
#             # just for debugging
#             print("\n\nReceived request")
#             print("======================")
#             print(request.rstrip())
#             print("======================")
#
#             print("\n\nReplied with")
#             print("======================")
#             print(reply.rstrip())
#             print("======================")
#
    return 0
#
# # will be a significant part of the lab
# # take in the ascii representation, verify it's correctly formatted according to html standards
# # either attempt to fulfill the request (if it's for our html file), in which case we form the correctly formatted reply
# # a lot of string processing (python.split is out friend)
# def http_handle(request_string):
#     """Given a http request return a response
#
#     Both request and response are unicode strings with platform standard
#     line endings.
#     """
#
#     assert not isinstance(request_string, bytes)
#
#     # Fill in the code to handle the http request here. You will probably want
#     # to write additional functions to parse the http request into a nicer data
#     # structure (eg a dict), and to easily create http responses.
#     CS460_TODO
#
#     raise NotImplementedError
#
#     pass
#

if __name__ == "__main__":
    sys.exit(main())
