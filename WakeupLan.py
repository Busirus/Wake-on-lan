import socket

def wake_on_lan(mac_address):
    # Construit le paquet Wake-on-LAN
    # Le paquet est composé de 6 octets de données 0xFF suivis de l'adresse MAC de l'ordinateur cible 16 fois
    data = b"\xff" * 6 + (mac_address * 16).encode()

    # Envoie le paquet UDP à l'adresse broadcast 255.255.255.255 sur le port 9
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, ("255.255.255.255", 9))

# Réveille l'ordinateur avec l'adresse MAC saisie
host = input("Adresse MAC de l'ordinateur à réveiller : ")
wake_on_lan(host)