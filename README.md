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
> [!WARNING]
> Don't use port 8338 for Routing Server.

### Run the server

 ```ps
python3 mserver.py
```

### Extra Note

#### *1 Server IP

Server IP address is required for configuration(selfip), server ip can be found using:

For Windows:
```ps
ipconfig
```
> [!note]
> If the Routing Server is running on same computer as that of Command and Control Server then ccserver should be: `http://127.0.0.1:8338/` however selfip should be actual network IP (or the public IP if hosted on cloud) of the computer and not any localhost.
