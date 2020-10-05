"""
 ! SERVER File
 ? Bind to socket and listen for client message, decrypt client message and provide encryption keys

 Project by Abhinav Robinson
"""


# Import python socket, random, sympy, hashlib, pickle module
import hashlib
import pickle # Pickle arrays to transport over sockets
import random
import socket
import sympy # Sympy is imported to generate prime numbers efficiently

#Local import to generate keys
from generate_keys import generate


# Connect and recieve message
def server_init():

    # Take prime upper bound
    if __debug__ == True: PRIME_LIMIT = int(input("Enter PRIME the upper bound (1000,1000000000) - (Higher is better): "))
    else: PRIME_LIMIT = 6000

    # Generate Key Pair
    e, d, n = generate(sympy.randprime(1, PRIME_LIMIT),
                       sympy.randprime(1, PRIME_LIMIT))

    # Show keys
    assert __debug__ ,f"Encryption Key: {e} \n Mod Key: {n} \n Secret Key: {d}"

    # Initialize socket
    s = socket_init(port=6000, clients=1)

    # Listen for client message
    while True:

        # Get client socket and address
        clientsocket, address = s.accept()

        # Print Connection details
        print(f"Connection to {address} established!")

        # Send Encryption key (public)
        clientsocket.send(bytes(str(e), "utf-8"))

        # Send Mod Key (public)
        clientsocket.send(bytes(str(n), "utf-8"))

        # Recieve pickle data stream
        data_string = clientsocket.recv(4096)

        if __debug__ == True:
            # Recieve Original Hex value (debug for verification)
            hex_encoded = clientsocket.recv(1024)

            # Decode Hex from UTF-8
            public_hex_value = hex_encoded.decode("utf-8")

        # Pickle -> array
        signed_msg = pickle.loads(data_string)

        # Give confirmation
        assert __debug__, f"Authentication Status: True \n Recieved: {signed_msg}"
        # Decrypt using private key
        hex_value = decrypt(signed_msg, d, n)

        # Show decrypted Hex Value
        print(f"Decrypted Hash Value: {hex_value}")

        # Integrity Check
        if hex_value == public_hex_value and __debug__ == True:
            # Success
            print("Integrity Status : True")
            break
        else: 
            # Debug might be FALSE
            print("Integrity Status : Not Verified")
            break
    #End of while loop

    # Close Connections / Cleanup
    clientsocket.close()
    s.close()

# EOF


# Decrpytes Hex from RSA Scheme
def decrypt(ctext, d, n):

    try:
        # Decrypt Hex Array from Encrypted Array
        text = [chr(pow(int(char), d, n)) for char in ctext]

        # Returns String
        return "".join(text)

    # Catch Exception
    except TypeError as e:
        print(e)

# EOF


# Initializes socket at given port of n clients
def socket_init(port = 6000, clients = 1):

    # Initialize socket stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Indicate initialisation
    print("Socket stream initialised as TCP/IP")

    # Specify port
    server_port = port

    # Bind to port
    sock.bind((socket.gethostname(), server_port))

    # Listen for 1 client connection
    sock.listen(clients)

    # Server init message
    print(f"Server initialised and listening to Port:{server_port}")

    # return socket
    return sock

# EOF


# Run function for connection
try:
    server_init()
except AssertionError as AE:
    print("Internal Server Error : Debug Failure")
finally:
    print("Server successfully closed.")


# End of server.py