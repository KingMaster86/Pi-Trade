# Pi Trade: Automated Cryptocurrency Trading Bot for Pi Network

Pi Trade is an automated Python-based trading bot designed to trade on the Pi Network. It interacts with the Pi Network's API (or a custom wrapper if API support is not available) and executes buy and sell orders on multiple trading pairs.

The bot uses a simple trading strategy where it buys when the price drops by 1% in the last 5 minutes and sells when the price increases by 1%. This strategy helps automate trading actions based on market fluctuations and provides users with a way to participate in trading without manual intervention.

## Supported Trading Pairs

Pi Trade supports multiple Pi Network trading pairs:

- PI NETWORK/BTC
- PI NETWORK/USDT
- PI NETWORK/ETH
- PI NETWORK/USDT
- PI NETWORK/TRON
- PI NETWORK/DOGECOIN
- PI NETWORK/DIGIBYTE
- PI NETWORK/BINANCE

## Features

- **Automated Trading**: The bot automatically executes buy and sell orders based on the defined price change strategy.
- **Multiple Trading Pairs**: Trade across various pairs such as PI NETWORK/BTC, PI NETWORK/USDT, and more.
- **Simple Trading Strategy**: Buy when the price drops by 1%, and sell when the price rises by 1% from the initial price.
- **Customizable**: You can adjust trading amounts and time intervals to suit your preferences.

## Setup and Installation

### Requirements

1. Python 3.x
2. Install the required Python libraries:
   ```bash
   pip install ccxt
