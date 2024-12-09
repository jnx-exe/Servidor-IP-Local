import http.server
import socketserver
import socket

port = 8084

manejador = http.server.SimpleHTTPRequestHandler

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

with socketserver.TCPServer((local_ip, port), manejador) as httpd:
    print(f"Servidor iniciando en la IP {local_ip}y en el {port}")
    print(f"Accede a el desde tu navegador en : http://{local_ip}:{port}")

    httpd.serve_forever()
