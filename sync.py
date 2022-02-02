import json
from websocket import create_connection

CLIENT_ID = "EXjnCvwy"
CLIENT_SECRET = "x8cjpn1t5zQlG-gi68zpv4AIac8iOQ8VDw4bz_DFGyQ"

auth_dict = {"method": "public/auth", "params": {"client_id": CLIENT_ID,
                                                 "client_secret": CLIENT_SECRET,
                                                 "grant_type": "client_credentials"}}

if __name__ == "__main__":
    ws = create_connection("wss://test.deribit.com/ws/api/v2/")
    ws.send(json.dumps(auth_dict))
    print(ws.recv())
    # -->SUBSCRIBE TO STREAMS HERE<--
    ws.close()
