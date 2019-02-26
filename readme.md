# Private DDNS for DigitalOcean

This is a tiny project (a python script tbh) which you can use to update your DNS A record.

# Problem 
One main issue setting up a small web server of VPN server at home is managing your public IP. Most home ISPs do charge extra for issuing you a static public IP address. If you do not want to pay then you need to tackle this problem yourself.

# Solution
You can setup a subdomain/domain with your home address. Here, I have written a tiny script which checks if my current home IP has changed. If positive, it updates the DNS records associated with my domain. 

I manage my DNS with digitalocean (www.digitalocean.com = DO). DO provides a REST api which can be used to update your configuration. 

# How to run

You can run the file 'ddnsApp.py' using Python 3. I have set up a cron job to make my script run every 15 minutes to check a change in IP address. 

The file 'private_info.txt' contains your current IP address


