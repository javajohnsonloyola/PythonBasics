from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Jacob's Kitchen & Travels YouTube channel"

@app.route("/about")
def about():
    return "This is Jacob's Kitchen & Travels "

@app.route("/contact")
def contact():
    return "https://www.youtube.com/watch?v=6UU18kjGEq4&t=294s"

@app.route("/services")
def services():
    return "We provide cooking tutorials, travel vlogs, and family-friendly content."

@app.route("/help")
def help_page():
    return "Make sure to subscribe to our channel and hit the notification bell for updates on new videos!"
if __name__ == "__main__":
    app.run(debug=True)