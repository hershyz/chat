import requests

name = input("chatroom name: ")

while True:
    message = input("> ")
    if (len(message) > 0):
        payload = {
            "message": message,
            "name": name
        }
        r = requests.post("http://127.0.0.1:5000/send", json=payload)