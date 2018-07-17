from socketserver import BaseRequestHandler, TCPServer
import socket


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("Got Connection from--->", self.client_address)
        while True:
            msg = self.request.recv(8129)
            print(msg)
            if not msg:
                break
            self.request.send(msg)


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8899))
    s.listen(5)
    while True:
        conn, name = s.accept() # 返回建立的链接
        print(conn.recv(1024))
        conn.sendall(b'''HTTP/1.1 200 OK

        <html>
          <head>
            <title>Build A Web Server</title>
          </head>
          <body>
            Hello World, this is a very simple HTML document.
          </body>
        </html>

        ''')
        conn.close()


if __name__ == '__main__':
    server()
