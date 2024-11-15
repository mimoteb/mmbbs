from flask import Flask, request, render_template_string
import socket
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get client IP
    client_ip = request.remote_addr
    
    # Get server IP (the IP of the machine running this Flask app, specifically eth0 interface)
    server_ip = os.popen('ip -4 addr show eth0 | grep -oP "(?<=inet\s)\d+(\.\d+){3}"').read().strip()
    server_ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
    # Collect request data
    request_data = {
        'method': request.method,
        'headers': dict(request.headers),
        'args': request.args,
        'form': request.form,
        'json': request.get_json(silent=True),
        'client_ip': client_ip
    }

    # Log request data
    app.logger.info(f"Request Data: {request_data}")

    # Render HTML template with server and client IPs
    html_template = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Server and Client Information</title>
      </head>
      <body>
        <h1>Request received successfully</h1>
        <p>Antwort Vom Server IP: {{ server_ip }}</p>
        <p>Client IP: {{ client_ip }}</p>
      </body>
    </html>
    """

    return render_template_string(html_template, server_ip=server_ip, client_ip=client_ip)

if __name__ == '__main__':
    # Run the app on port 5000 (commonly used for Flask apps)
    app.run(host='0.0.0.0', port=5000, debug=True)
