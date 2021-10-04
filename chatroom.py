import time
import requests

last_index = 0

while True:
    
    message_request = requests.get("http://127.0.0.1:5000/get_last_message")
    message = message_request.text
    index_request = requests.get("http://127.0.0.1:5000/get_last_index")
    index = index_request.text
    
    if index != last_index and message != "Null":
        print(message)
        last_index = index

    time.sleep(0.1)