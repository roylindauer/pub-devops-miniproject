from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Favorite dessert:</b> {favorite_dessert}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), favorite_dessert=os.getenv('FAVORITE_DESSERT', 'all of them'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)