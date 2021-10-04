from flask import Flask, request

app = Flask(__name__)
messages = []

@app.route("/")
def home():
    return "no args"

@app.route("/send", methods=["POST"])
def send():
    try:
        data = request.get_json()
        name = data['name']
        message = data['message']
        messages.append("[" + str(name) + "]: " + str(message))
        return "success"
    except:
        return "internal error"

@app.route("/update", methods=["GET"])
def update():
    return str(messages)

@app.route("/get_last_message", methods=["GET"])
def get_last_message():
    if len(messages) > 0:
        return str(messages[len(messages) - 1])
    else:
        return "Null"

@app.route("/get_last_index", methods=["GET"])
def get_last_index():
    return str(len(messages))

if __name__ == "__main__":
    app.run()