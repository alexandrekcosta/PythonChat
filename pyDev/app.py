from flask import Flask,render_template
from flask_socketio import SocketIO,send

app = Flask(__name__,template_folder="/home/xubuntu/PycharmProjects/pyDev/")
app.config["SECRET"] = "tudoaleatoriokkk"
app.config["DEBUG"] = True
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on("message")
def manage_message(message):
    print(f"Message: {message}")
    send(message,broadcast=True)

@app.route("/")
def home():
    return render_template('homepage.html')

if __name__ == "__main__":
    socketio.run(app,host='localhost')