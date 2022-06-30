# A command line client for the date server.
import sys
import socket

if len(sys.argv) != 2:
    print('Pass the server IP as the sole command line argument')
else:
    #AF_INET means the networking layer underneath is IPv4. Other possible values are AF_UNIX, AF_INET6, AF_BLUETOOTH, and others.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((sys.argv[1], 59898))
        print('Enter email address then Ctrl+D or Ctrl+C to quit')
        while True:
            line = sys.stdin.readline()
            if not line:
                # End of standard input, exit this entire script
                break
            sock.sendall(f'{line}'.encode('utf-8'))
            def Data():

                while True:
                    email = sock.recv(128)
                    Name = sock.recv(128)
                    print(Data().decode("utf-8"), end='')
                    if len(Data()) < 128:

                        # No more of this message, go back to waiting for next message
                       break
