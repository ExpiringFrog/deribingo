import json
import pprint
from lib.websocket import *

# add your authentication keys for Deribit's testnet here.
CLIENT_ID = ""
CLIENT_SECRET = ""


def on_message(ws, message: str):
    """
    This function receives a callback when the server you're connected to sends a message.
    When the incoming message is a response indicating a successful authentication,
    we can subscribe to data streams.
    :param ws: the WebSocketApp class object that does the callback
    :param message: the incoming message as string
    """
    message_dict = deserialize(message)
    if "result" in message_dict.keys() and "access_token" in message_dict["result"].keys():
        # -->SUBSCRIBE TO STREAMS HERE<--
        # ws.send(subscription_stream)
        pass
    prettyprint(message)


def on_error(ws, error):
    """
    This function receives a callback if the server deems an incoming message
    invalid.
    :param ws: the WebSocketApp class object that does the callback
    :param error: Exception object
    """
    print(error)


def on_close(ws, close_status_code, close_msg):
    """
    This function receives a callback if the server closes the connection.
    :param ws: the WebSocketApp class object that does the callback
    :param close_status_code: int
    :param close_msg: str
    """
    print("Connection closed.")


def on_open(ws):
    """
    This function receives a callback when a websocket connection gets established.
    We authenticate the connection in this function, before we send any other requests.
    :param ws: the WebSocketApp class object that does the callback
    """
    auth_dict = {"method": "public/auth", "params": {"client_id": CLIENT_ID,
                                                     "client_secret": CLIENT_SECRET,
                                                     "grant_type": "client_credentials"}}
    ws.send(serialize(auth_dict))


def serialize(message_dict):
    return json.dumps(message_dict)


def deserialize(message_string):
    return json.loads(message_string)


def prettyprint(message_dict):
    pprint.pprint(message_dict)


if __name__ == "__main__":
    # make sure to connect to testnet, not to live trading
    ws = WebSocketApp("wss://test.deribit.com/ws/api/v2/",
                      on_open=on_open,
                      on_message=on_message,
                      on_error=on_error,
                      on_close=on_close)

    # this function blocks indefinitely, all logic should be done in callback functions
    ws.run_forever()
