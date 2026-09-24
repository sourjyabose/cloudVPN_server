# Routing Server

### Install Requirements

```ps
python3 -m pip install -r requirements.txt
```
### Things to change before running

In the .env file change the following:

```
ccserver=<URL of Command and Control Server>
selfip=<IP address of the computer that will run this server *1>
port=<port no you wish to use>
servername=<Jo man mai aaye wo (As entered during registration via Admin Dashboard)>
serverkey=<jaisi tumhari marzi (As entered during registration via Admin Dashboard)>
```

### Run the server

 ```ps
python3 mserver.py
```

### Extra Note

#### *1 Server IP

Server IP address is required for configuration, server ip can be found using:

For Windows:
```ps
ipconfig
```
