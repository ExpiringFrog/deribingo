import json
from lib.websocket import create_connection

CLIENT_ID = ""
CLIENT_SECRET = ""

auth_dict = {"method": "public/auth", "params": {"client_id": CLIENT_ID,
                                                 "client_secret": CLIENT_SECRET,
                                                 "grant_type": "client_credentials"}}

if __name__ == "__main__":
    ws = create_connection("wss://test.deribit.com/ws/api/v2/")
    ws.send(json.dumps(auth_dict))
    print(ws.recv())
    # -->SUBSCRIBE TO STREAMS HERE<--
    ws.close()
