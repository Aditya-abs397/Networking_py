
# Networking_py

A collection of low-level Python networking tools built from scratch ,focused on understanding protocols, sockets, and offensive network programming.
Inspired by Black Hat Python by Justin Seitz & Tim Arnold.


## Tools
### TCP Client & Server:

Raw TCP socket communication. Useful for testing services, debugging protocols, and understanding the handshake lifecycle.

### UDP Client & Server:

Connectionless socket communication. Covers stateless protocols, DNS-style interactions, and scenarios where speed > reliability.

### Netcat (netcat.py):

A Python reimplementation of the classic (nc) utility.

Supports : 
Command execution over sockets, file upload and interactive shell.

## Requirements

Python 3.6+

No third-party dependencies for current tools (stdlib only: socket, threading, argparse, subprocess)

## Disclaimer

For educational and authorized testing purposes only. Do not use against systems you don't own or have explicit permission to test.

## References

Black Hat Python, 2nd Ed. — Seitz & Arnold

The Cyber Mentor Ethical HAcking Course Part 1: https://www.youtube.com/watch?v=3FNYvj2U0HM&t=20113s

Elevate Cyber BHP course: https://www.youtube.com/watch?v=98F-4HoNaDU&list=PLk6vOUIjcauWAzYx5zn5JTnDL9R-Osk_H&index=7

Python docs: https://docs.python.org/3/library/

### Author
Aditya Salunke