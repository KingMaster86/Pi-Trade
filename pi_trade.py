import ccxt
import time

# Konfigurasi API
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Menggunakan PI Network jika didukung oleh ccxt atau pengaturan kustom lainnya
exchange = ccxt.pinetwork({
    'apiKey': api_key,
    'secret': api_secret
})

# Daftar pasangan mata uang yang akan diperdagangkan
symbols = [
    'PI NETWORK/BTC',
    'PI NETWORK/USDT',
    'PI NETWORK/ETH',
    'PI NETWORK/USDT',
    'PI NETWORK/TRON',
    'PI NETWORK/DOGECOIN',
    'PI NETWORK/DIGIBYTE',
    'PI NETWORK/BINANCE'
]

# Jumlah yang ingin diperdagangkan untuk setiap pasangan
amount = 10  # Contoh jumlah, sesuaikan dengan kebutuhan

# Fungsi untuk mendapatkan harga terkini
def get_current_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

# Fungsi untuk melakukan pembelian
def buy_order(symbol, price):
    order = exchange.create_market_buy_order(symbol, amount)
    print(f"Buy order executed for {symbol} at {price}")
    return order

# Fungsi untuk melakukan penjualan
def sell_order(symbol, price):
    order = exchange.create_market_sell_order(symbol, amount)
    print(f"Sell order executed for {symbol} at {price}")
    return order

# Fungsi untuk cek dan eksekusi strategi trading
def trade_strategy(symbol):
    initial_price = get_current_price(symbol)
    print(f"Initial price for {symbol}: {initial_price}")

    # Menunggu 5 menit untuk mendapatkan harga terbaru
    time.sleep(300)

    current_price = get_current_price(symbol)
    print(f"Current price after 5 minutes for {symbol}: {current_price}")

    # Menentukan perubahan harga
    price_change = (current_price - initial_price) / initial_price * 100
    print(f"Price change for {symbol}: {price_change}%")

    # Jika harga turun 1%, beli
    if price_change <= -1:
        buy_order(symbol, current_price)
        return 'bought', current_price
    # Jika harga naik 1%, jual
    elif price_change >= 1:
        sell_order(symbol, current_price)
        return 'sold', current_price
    else:
        print(f"No action for {symbol}. Price change is too small.")
        return 'no action', current_price

# Main loop untuk menjalankan strategi secara berulang untuk setiap simbol
def main():
    while True:
        for symbol in symbols:
            print(f"Starting trading strategy for {symbol}...")
            action, price = trade_strategy(symbol)
            if action != 'no action':
                print(f"Action taken for {symbol}: {action} at price {price}")
            else:
                print(f"No action for {symbol}. Current price: {price}")
            time.sleep(60)  # Menunggu 1 menit sebelum memulai iterasi berikutnya

if __name__ == '__main__':
    main()
