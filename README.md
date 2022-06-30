# Server-client
Goal: Virtualize a communication of serialized/data between 2 components
 

Consider the following dataclass code that should be serialized before transfer
class ClientData

string name
string email

Write a client/server pseudo application showing that your software complies with all of the following objectives

Application should send serialized ClientData from Server to Client

Use at least 2 instances of Client

Client displays received data in the console

ClientData from the server is using user input for its data

(Bonus) Email format should be verified (e.g. containing a @ then a .)

(Bonus) Name should be at least 4 characters and spaces should be converted to _



Design constrains:
Application should be designed using Object Oriented Programming
Application should use the Observer Design Pattern
Application should contain at least 1 abstraction
No network/real socket communication, the Socket should send a ClientData to different Client instances in the same program
 
