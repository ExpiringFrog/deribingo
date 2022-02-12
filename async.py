import json
from lib.websocket import *

CLIENT_ID = ""
CLIENT_SECRET = ""


def on_message(ws, message):
    message_dict = json.loads(message)
    if "result" in message_dict.keys() and "access_token" in message_dict["result"].keys():
        # -->SUBSCRIBE TO STREAMS HERE<--
        pass
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Connection closed.")


def on_open(ws):
    auth_dict = {"method": "public/auth", "params": {"client_id": CLIENT_ID,
                                                     "client_secret": CLIENT_SECRET,
                                                     "grant_type": "client_credentials"}}
    ws.send(json.dumps(auth_dict))


if __name__ == "__main__":
    ws = WebSocketApp("wss://test.deribit.com/ws/api/v2/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
