# Deribingo example

This repository contains two small examples showing how to connect to Deribit using the Websocket protocol.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

```bash
pip install -r requirements.txt
```

## Setup

Replace CLIENT_ID and CLIENT_SECRET with the values you received and run both scripts. The console should show something like 
```json
{"jsonrpc":"2.0","result":{"token_type":"bearer","scope":"account:read_write block_trade:read_write connection custody:read_write mainaccount trade:read_write wallet:read_write","refresh_token":"XXXXX","expires_in":31536000,"access_token":"XXXXX"},"usIn":1643798543728896,"usOut":1643798543729367,"usDiff":471,"testnet":true}

```
If the console instead shows
```json
{"jsonrpc":"2.0","error":{"message":"invalid_credentials","code":13004},"usIn":1643798691312610,"usOut":1643798691312668,"usDiff":58,"testnet":true}
```
recheck your credentials or ask for help.

## Usage

There are two ways to deal with open connections: synchronously or asynchronously. The asynchronous method as shown in `async.py` uses callbacks whenever the websocket client receives an event. When a connection gets established, `on_open` gets called. When a message is received, `on_message` gets called, etc. This is useful for listening to continuously streaming data. You can filter for wanted messages in the `on message` callback function like so:

```python
def on_message(message):
    if message_of_relevant_type(message):
        handle_message(message)
    else:
        return 
```
The other method, the synchronous method, is more suitable for simple request/response style communication. This method is shown in `sync.py`. A request can be sent by adding a `ws.send()` followed by a blocking `ws.recv()` to get the response.

In both files an example request is given: the authentication.