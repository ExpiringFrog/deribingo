import json
import time
from lib.websocket import WebSocketApp

CLIENT_ID = ""
CLIENT_SECRET = ""

    
def on_message(ws, message): 
  result = get_result(message) 
 
  if is_authenticated(ws, result): 
    print("authenticated") 
 
  # --> PARSE STREAM RESULT HERE <-- 
 
def on_open(ws): 
  authenticate(ws)

  # --> SUBSCRIBE TO STREAM HERE <--

def on_error(ws, error):
  pass

def on_close(ws, close_status_code, close_msg):
  print("Connection closed.")


# ---------------------> HELPER FUNCTIONS <-------------------------

def ws_send(ws, msg):
  ws.send(serialize(msg))

def is_authenticated(ws, msg):
  return "access_token" in msg.keys()

def authenticate(ws):
  msg = {
    "method": "public/auth", 
    "params": {
      "client_id": CLIENT_ID,
      "client_secret": CLIENT_SECRET, 
      "grant_type": "client_credentials"}
  }
  ws_send(ws, msg)
  

def get_result(msg):
  deserialized_msg = deserialize(msg)

  if 'error' in deserialized_msg:
    pprint(deserialized_msg)
    raise Exception()

  if 'result' in deserialized_msg:
    return deserialized_msg['result']

  if 'params' in deserialized_msg:
    return deserialized_msg['params']
  raise Exception('Unknown message')

def serialize(msg):
  return json.dumps(msg)

def deserialize(msg):
  return json.loads(msg)

def pprint(obj):
  if isinstance(obj, str):
    obj = json.loads(obj)
  print(json.dumps(obj, sort_keys=True, indent=4))

if __name__ == "__main__":
  ws = WebSocketApp("wss://test.deribit.com/ws/api/v2/",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

  ws.run_forever()
