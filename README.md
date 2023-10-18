# Deribingo

The goal of this competition is to achieve bingo (i.e., a straight line of four cells) on the 'Deribingo' card, `bingocard_final.pdf`. Detailed explanations of each bingo cell/goal can be found [here](https://docs.google.com/document/d/1Oy7x9-gnVWtSWdc9Lv9OxfJLfyjU_mMeKO6PzLIrAqo/edit?usp=sharing).

The competition has a max duration of 2 hours.

## Introduction
This instruction document explains on how to: 
- Setup the code in the [Setup](##setup) section.
- Authenticate with the Deribit API in the [Authentication](##authentication) section.
- How to work with the Deribit API in a synchronous or asynchronous manner using the websocket protocol in the [Usage](#usage) section.

## Setup

If you do not already have them installed, you can install the dependencies with the following steps depending on your Operating System (OS).

You're going to download and install Git and Python 3.8.2:

OS   |      Python 3.8.2      |  Git |
---------|:-------------:|------:|
Windows 10 |  [Installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe) | [Installer](https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/Git-2.35.1.2-64-bit.exe) |
macOS |    [Installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg)   |   [Instructions](https://git-scm.com/download/mac) |
Linux | [Instructions](#) |   [Instructions](https://git-scm.com/download/linux) |


### Get the source
Clone the deribingo repository into your current directory:
```bash
git clone https://github.com/ExpiringFrog/deribingo.git
```

## Authentication
Once every dependency is installed and the source is downloaded, you can try to authenticate to the Deribit API.
You can get your `CLIENT_ID` and `CLIENT_SECRET` by selecting the row with the number you received from [here](https://docs.google.com/spreadsheets/d/1rz8O8k2xWzuQ189LzhWOUh3grIonuDZ2flDA-h6fzf4/edit?usp=sharing). 

Be sure to copy the credentials from the right row, because if someone shares the same key you might get undesired results and lose the competition.

Replace `CLIENT_ID` and `CLIENT_SECRET` with the values you received and run both scripts. The console should show `authenticated`. 
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

### SSL issues

If you have SSL certificate issues you can replace: 
A line in async.py with: `ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})`
A line in sync.py with: `ws = create_connection("wss://test.deribit.com/ws/api/v2/",sslopt={"cert_reqs": ssl.CERT_NONE})` 

And add `import ssl` at the top of the script.

## Debugging

You can debug with:
- The IDE of your choice
- `pdb`. For example `python3 -m pdb sync.py`
- `print()` statements

## Tips

- Start by analyzing the bingo card and documentation, so you can choose the fastest way to get a bingo.
- Your code only needs to work for the 2 hours of the challenge, so don't waste time by making the code too general. The code can be very ugly.
- Try to evaluate your solution for your current bingo goal step-by-step instead of trying all steps at once.
- Make sure you understand the code of both `sync.py` and `async.py`.
