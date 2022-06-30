# A server program which accepts requests from clients to valiadate strings . When
 # clients connect, a new thread is started to handle a client. The receiving of the
 # client data, the validation, and the sending back of the data is handled on the
 # worker thread, allowing much greater throughput because more clients can be handled
 # concurrently.

import socketserver
import threading
import re

#The server we are using here is a class extending both TCPServer and ThreadingMixIn.
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

# Email and name will be validate here and then written back to the client.
class ClientData(socketserver.StreamRequestHandler):

    def handle(self): #abstraction for the componenets
        client = f'{self.client_address} on {threading.currentThread().getName()}'
        print(f'Connected: {client}')
        while True:
            #email valiadtion using Regex
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            email = self.rfile.readline()
            if not email:
                break

            def isValid(email):
                if re.fullmatch(regex, email):
                    print("Valid email")
                else:
                    print("Invalid email")
            self.wfile.write(email.decode('utf-8').encode('utf-8'))
            # Name validation for at least four chacters
            Name = self.rfile.readline()
            def isNamevalid(Name):
                if len(Name) < 4:
                    reason = ('Name must be greater than 4 characters')
                    return '', reason
                else:
                    return Name, ''
                self.wfile.write(Name.decode('utf-8').encode('utf-8'))

                print(f'Closed: {client}')

with ThreadedTCPServer(('', 59898), ClientData) as server:
    print(f'The ClientData server is running...')
    server.serve_forever()