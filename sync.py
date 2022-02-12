import json
import pprint
from lib.websocket import create_connection

CLIENT_ID = ""
CLIENT_SECRET = ""


def authenticate(ws):
    """
    This function authenticates a websocket connection
    :param ws: WebSocket object
    """
    auth_dict = {"method": "public/auth", "params": {"client_id": CLIENT_ID,
                                                     "client_secret": CLIENT_SECRET,
                                                     "grant_type": "client_credentials"}}
    ws.send(serialize(auth_dict))


def serialize(message_dict):
    """
    This function takes a dictionary and json serializes it
    :param message_dict: dict
    :return: str
    """
    return json.dumps(message_dict)


def deserialize(message_string):
    """
    This function takes a string and deserializes it to a dictionary.
    :param message_string: str
    :return: dict
    """
    return json.loads(message_string)


def prettyprint(message_dict):
    """
    This function prints a dictionary in a easily readable format.
    :param message_dict: dict
    """
    pprint.pprint(message_dict)


if __name__ == "__main__":
    # make sure to connect to testnet, not to live trading
    ws = create_connection("wss://test.deribit.com/ws/api/v2/")

    # after we successfully authenticate the connection, we can start sending other requests
    authenticate(ws)
    response = deserialize(ws.recv())
    prettyprint(response)

    # SEND OTHER REQUESTS HERE
    # ws.send(serialize(request_dict))

    ws.close()
