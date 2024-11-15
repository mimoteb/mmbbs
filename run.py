from flask import Flask, request, render_template_string
import socket
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    server_ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
    # Determine color based on server IP
    col = ""
    if str(server_ip).endswith("101"):
        col = 'red'
    elif str(server_ip).endswith("102"):
        col = 'blue'
    elif str(server_ip).endswith("103"):
        col = 'green'
    html_template = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Reverse Proxy && Load Balance Web01, Web02, und Web03</title>
      </head>
      <body>
        <h1><p class="{{col}}">Antwort Vom Server IP: {{ server_ip }}</p></h1>
        <p>Web01: 192.168.199.101</p>
        <p>Web02: 192.168.199.102</p>
        <p>Web03: 192.168.199.103</p>
        <p>Reverse Proxy Server: 192.168.199.100<p>
        
      </body>
    </html>
    """

    return render_template_string(html_template, server_ip=server_ip, col=col)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
