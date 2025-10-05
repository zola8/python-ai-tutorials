# https://www.youtube.com/watch?v=3NEzo3CfbPg

import hashlib
import socket
import sqlite3
import threading

conn = sqlite3.connect("userdata.db", check_same_thread=False)
cur = conn.cursor()


def handle_connection(client):
    # TODO encrypt the connection
    client.send("Username: ".encode("utf-8"))
    username = client.recv(1024).decode("utf-8")
    client.send("Password: ".encode("utf-8"))
    password = client.recv(1024)
    password = hashlib.sha256(password).hexdigest()
    # TODO sqlite connection again in client
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    if cur.fetchall():
        client.send("Login successful.".encode("utf-8"))
        # secrets, services...
    else:
        client.send("Login failed.".encode("utf-8"))


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # internet socket , tcp protocol
    server.bind(("localhost", 9999))
    server.listen()
    print("Server listening...")

    while True:
        client, address = server.accept()
        threading.Thread(target=handle_connection, args=(client,)).start()
