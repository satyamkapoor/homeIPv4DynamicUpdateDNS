# Private DDNS for DigitalOcean

This is a tiny project (a python script tbh) which you can use to update your DNS A record.

I have a raspberry pi at home on which I have setup a VPN server. Unfortunately like most residential ISP my IPS changes my IP address at regular intervals due to which I have to change the configuration of my ovpn client files myself. 

To combat this issue I have written this python script which checks if the local IPV4 is changed or not, and if changed updated the A record of my domain associated with my pi. As I use digitalocean for my DNS record management. I have written the script for DO. In future I will update it to work with AWS and Google Cloud. 


