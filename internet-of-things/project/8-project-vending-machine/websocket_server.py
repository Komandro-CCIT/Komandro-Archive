import json
import traceback

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from cores.websocket_event import WebsocketEvents


class Server(WebSocket):
    clients = []
    websocket_events = WebsocketEvents(None, {})

    def handleMessage(self):
        try:
            if self.data:
                data = json.loads(self.data)
                if "event" in data and data["event"]:
                    self.websocket_events.event = data["event"]
                    self.websocket_events.payload = data["values"]

                    result = self.websocket_events.execute()
                    if result:
                        self.data = json.dumps(result)

            print(self.address[0] + " - " + self.data)
            for client in self.clients:
                client.sendMessage(self.data)
        except Exception as e:
            print(e)

    def handleConnected(self):
        self.clients.append(self)
        for client in self.clients:
            client.sendMessage(self.address[0] + " - connected")
        print(self.address, "connected")

    def handleClose(self):
        self.clients.remove(self)
        for client in self.clients:
            client.sendMessage(self.address[0] + " - disconnected")
        print(self.address, "closed")


host = "0.0.0.0"
port = "3333"
server = SimpleWebSocketServer(host, port, Server)

while True:
    try:
        print(f"Websocket running on {host}:{port}")
        server.serveforever()
    except Exception as e:
        print(e)
