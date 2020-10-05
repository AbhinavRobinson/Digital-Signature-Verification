# RSA-over-SHA1

Encrypt message and generate signature on Sender, and decrypt and ensure message integrity on receiver.

## Requirements

- sympy
- python3

## Usage

- bootup server running `python3 server.py`
- send client message by running `python3 client.py`

## Features

- [X] Server and Client Setup  
- [X] Code Review and Commentted  
- [X] Add Digital Signatures  
- [X] Encrypt using RSA  
- [X] Client side decryption  
- [X] Show validation messages
- [X] Added DEBUG features

## TODO

- [ ] Move prime number generation out of server to generate_keys.
- [ ] Remove enter PRIME_LIMIT function.
- [ ] Abstract code and genralise.

## Possible Addons (contributions)

- [ ] Refactor code to a more Stateful paradigm? (Hard) #3
- [ ] Testing Scripts. (medium) #2
- [X] Rework __DEBUG__ python for additional debug features. (medium) #1
- [ ] Add more comments for documentation. (supa-ez) #0
