import socket
import requests
import select
import threading
import queue
import random
import multiprocessing
from dotenv import load_dotenv
import os
import requests


load_dotenv()

ccserver=os.getenv("ccserver")
selfip=os.getenv("selfip")
portfromenv=os.getenv("port")
servername=os.getenv("servername")
serverkey=os.getenv("serverkey")

if requests.get(f"{ccserver}/selfRegister/{servername}/{serverkey}/{selfip}/{portfromenv}").json()["status"]!="success":
    exit()


def noprint(*args):
    pass

print=noprint
def new_server(towardsclient,addr):
        
        datapackets=queue.Queue();
        socketstorage={}

        def targettoserverqueue(targetsock,ip,port,magnum):
            
            while True:
                
                try:
                    data=targetsock.recv(4096000)
                    if(data!=b''):
                        print(f"Apennding {ip} {port} {magnum}")
                        datapackets.put(b"jiolinkXoXoXoXsourjyakrishna"+f"{ip} {port} {magnum}".encode()+b"VooXoBsourjyaraushan"+data)
                except Exception as e:
                    print(e)
                    break;

        def receivefromclientandsendtotarget():
            secondbuff=b''
            print("function started")
            while True:
                rawdata=secondbuff+towardsclient.recv(1000000000)
                buf1=rawdata.split(b"jiolinkXoXoXoXsourjyakrishna")
                secondbuff=b'jiolinkXoXoXoXsourjyakrishna'+buf1[len(buf1)-1]
                buf1[len(buf1)-1]=b''
                for cdpack in buf1:
                    if(cdpack==b''):
                        continue;
                    payloadheader,payloaddata=cdpack.split(b"VooXoBsourjyaraushan")
                    payloadheader=payloadheader.decode()
                    payloadheader=payloadheader.split()
                    try:
                        socketstorage[int(payloadheader[2])].sendall(payloaddata)
                        print("Sent Data",payloadheader)
                    except Exception as e:
                        print(e)
                        print("Creating socket",int(payloadheader[2]))
                        servertotarget=socket.socket()
                        servertotarget.connect((payloadheader[0],int(payloadheader[1])))
                        socketstorage[int(payloadheader[2])]=servertotarget;
                        socketstorage[int(payloadheader[2])].sendall(payloaddata)
                        print("Sent Created Data",payloadheader)
                        threading.Thread(target=targettoserverqueue,args=(servertotarget,payloadheader[0],int(payloadheader[1]),int(payloadheader[2]))).start()






        def senddatatoclient():
        # dpl=len(datapackets)
        # ind=0;
            while True:
                towardsclient.sendall(datapackets.get());
                #if(ind!=len(datapackets)):
                #   towardsclient.sendall(datapackets[ind]);
                #  print("packlen: ",len(datapackets))
                # ind+=1
        threading.Thread(target=receivefromclientandsendtotarget).start()
        threading.Thread(target=senddatatoclient).start();

if __name__=="__main__":
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    sock.bind(("0.0.0.0",int(portfromenv)))
    sock.listen(5);

    while True:
        towardsclient,addr=sock.accept()
        multiprocessing.Process(target=new_server,args=(towardsclient,addr,)).start();



