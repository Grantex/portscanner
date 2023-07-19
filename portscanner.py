from socket import *

def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('port %d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('port %d/tcp closed'%tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[×] Cannot resolve %s'%tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[] Scan result of: %s'%tgtName[0])
    except:
        print('\n[] Scan result of: %s'%tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port: %d'% tgtPort)
        conScan(tgtHost, int(tgtPort))




if __name__ == '__main__':
    portScan('google.com', [14, 22]) #input the domain name and port numbers you seek to scan for

#you can add an input function and GUI to create a port scanner app that shows what ports are open and closed