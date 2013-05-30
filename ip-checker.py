#!/usr/bin/env python

import requests
import smtplib

username = 'example1@gmail.com'
password = 'password'
toaddrs = 'example2@gmail.com'	#omit if using same to/from address

def get_current_ip():
	url = 'http://www.icanhazip.com'
	r = requests.get(url)
	ip_address = r.text
	return ip_address

def get_last_ip():
	ip = open('./ip.log', 'r')
	ip_address = ip.read()
	ip.close()
	return ip_address

def set_new_ip(ip_address):
	ip = open('./ip.log', 'w')
	ip.write(ip_address)
	ip.close()

ip_address = get_current_ip()
old_ip = get_last_ip()

if ip_address != old_ip:
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(username, username, ip_address)
	
	#omit next line if using same to/from address
	server.sendmail(username, toaddrs, ip_address)
	server.quit()
	set_new_ip(ip_address)
