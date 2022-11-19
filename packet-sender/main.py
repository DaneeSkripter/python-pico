import network
import socket
import time

ip = "10.42.0.1" # IP address
port = 1234 # Port
ssid = "fanda-hotspot" # Network name
password = "prosteheslo" #  Network password

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while sta.isconnected() == False:
    print("Pripojuji se k siti " + ssid)
    time.sleep(1)

if sta.isconnected():
    print("Pripojeno k siti " + ssid)
    
    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    zprava = input("Sem napiste zpravu co chcete napsat: ")
    if zprava == "c":
        port = input("Sem napiste novy port: ")
        print("Port byl zmenen na " + port )
        continue
    s.sendto(bytes(zprava, "utf-8"), (ip, int(port)))
    print("Zprava " + zprava + " byla odeslana")
    time.sleep(5)
