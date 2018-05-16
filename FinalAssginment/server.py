from websocket_server import WebsocketServer


def send_msg_allclient(client, server, message):
    server.send_message_to_all(message)


if __name__ == "__main__":
    bind_ip = "127.0.0.1"
    bind_port = 8080
    server = WebsocketServer(port=bind_port, host=bind_ip)
    server.socket.listen(5)

    server.set_fn_message_received(send_msg_allclient)
    server.run_forever()
