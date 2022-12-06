# Wake-on-lan

Ce code envoie un paquet UDP contenant les données appropriées à l'adresse broadcast 255.255.255.255 sur le port 9. Si l'ordinateur cible est configuré pour recevoir des paquets Wake-on-LAN et qu'il est en mode veille, il devrait être réveillé. Notez que pour que cela fonctionne, l'ordinateur cible doit être correctement configuré pour recevoir des paquets Wake-on-LAN et vous devrez connaître son adresse MAC.
