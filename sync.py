import json
import time

from lib.websocket import create_connection

CLIENT_ID = ""
CLIENT_SECRET = ""

ws = create_connection("wss://test.deribit.com/ws/api/v2/")

def authenticate(client_id: str, client_secret: str):
  msg = {
    "method": "public/auth", 
    "params": {
      "client_id": client_id,
      "client_secret": client_secret,
      "grant_type": "client_credentials"
      }
  }

  response = ws_send(msg)
  if 'access_token' in response:
    print('authenticated')

def ws_send(msg):
  ws.send(serialize(msg))
  response = json.loads(ws.recv())
  
  if 'error' in response:
    print(msg['method'])
    pprint(response)
  return response['result']

def serialize(msg):
  return json.dumps(msg)

def deserialize(msg):
  return json.loads(msg)

def pprint(obj):
  if isinstance(obj, str):
    obj = deserialize(obj)
  print(json.dumps(obj, sort_keys=True, indent=4))


if __name__ == "__main__":
    authenticate(CLIENT_ID, CLIENT_SECRET)
    # -->PUT YOUR REQUESTS HERE<--

    ws.close()
