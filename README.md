# Deribingo

The goal of this competition is to achieve bingo (i.e., a straight line of four cells) on the 'Deribingo' card, `bingocard.pdf`. Detailed explanations of each bingo cell/goal can be found [here](https://docs.google.com/document/d/1Oy7x9-gnVWtSWdc9Lv9OxfJLfyjU_mMeKO6PzLIrAqo/edit?usp=sharing).

The competition has a max duration of 2 hours.

## Introduction
This instruction document explains on how to: 
- Setup the code in the [Setup](##setup) section.
- Authenticate with the Deribit API in the [Authentication](##authentication) section.
- How to work with the Deribit API in a synchronous or asynchronous manner using the websocket protocol in the [Usage](#usage) section.

## Setup
### Replit
The easiest way to start is by using Replit, a browser-based Integrated Development Environment (IDE). You can fork the repository by signing up [here](REPLACE_ME).

### Locally
However, if you'd like to develop locally, you can follow the following steps depending on your Operating System (OS).

#### Windows
#### MacOS
#### Linux





## Authentication

Replace `CLIENT_ID` and `CLIENT_SECRET` with the values you received and run both scripts. The console should show something like: 
```json
{
    "jsonrpc":"2.0",
    "result": {
            "token_type": "bearer",
            "scope": "account:read_write block_trade:read_write connection custody:read_write mainaccount trade:read_write wallet:read_write",
            "refresh_token": "XXXXX",
            "expires_in": 31536000,
            "access_token": "XXXXX"
    },
    "usIn": 1643798543728896,
    "usOut": 1643798543729367,
    "usDiff": 471,
    "testnet": true
}

```
If the console instead shows:
```json
{
    "jsonrpc":"2.0",
    "error": {
        "message": "invalid_credentials",
        "code": 13004
    },
    "usIn": 1643798691312610,
    "usOut": 1643798691312668,
    "usDiff": 58, 
    "testnet": true
}
```
re-check your credentials or ask for help.

## Usage

There are two ways to deal with open connections: synchronously or asynchronously:   
- The synchronous method is more suitable for simple blocking request-response style communication. This method is shown in `sync.py`. A request can be sent by adding a `ws.send()` followed by a blocking `ws.recv()` to get the response.

- The asynchronous method as shown in `async.py` uses callbacks whenever the websocket client receives an event. When a connection gets established, `on_open` gets called. When a message is received, `on_message` gets called, etc. This is useful for listening to continuously streaming data. You can filter for wanted messages in the `on message` callback function like so:

```python
def on_message(message):
    if message_of_relevant_type(message):
        handle_message(message)
    else:
        return 
```
 
As a starting example, a simple authentication request is shown in the files `sync.py` and `async.py`.

## Implementation
Implement your solution in the `main.py` file. You can copy the contents of either example as starting point.

## Debugging

In Repl.it you can go to the debugger panel and add breakpoints to the code. Simply click on the run button to start debugging.

## Tips

- Your code only needs to work for the 2 hours of the challenge, so don't waste time writing your code too general.
- Make sure you understand the code from both examples.
- Start by analyzing the bingo card and documentation, so you can choose the fastest way to get a bingo.
