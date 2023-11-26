import configparser
import socket
import threading
import discord
import sqlite3
from parser import parse

config = configparser.ConfigParser()
config.read('config.ini')

db = sqlite3.connect("db.sqlite", check_same_thread=False)

# Discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Logged in as {client.user}')  

def start_bot():
  client.run(config ['discord'] ['token'])

# TCP Server

def start_server(host, port):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host, port))
  server.listen()

  print("Server listening on {}:{}".format(host, port))
  
  while True:
    client, client_address = server.accept()

    print("Connection from client {}".format(client_address))

    client_thread = threading.Thread(target=handle_client, args=(client,))
    client_thread.start()

def handle_client(client):
  replay = b''

  while True:
    chunk = client.recv(1024)
    
    if not chunk:
      break

    replay += chunk

  data = parse(replay)

  print(data)

  # Do something with the data here. Save it, post it, etc.

  cur = db.cursor()

  received = len(data)
  received = str(received)

  client.send(bytes(received, 'utf8'))
  client.close()

# Main

server_thread = threading.Thread(target=start_server, args=('127.0.0.1', 8080))
server_thread.start()

bot_thread = threading.Thread(target=start_bot)
bot_thread.start()

server_thread.join()
bot_thread.join()

db.close()