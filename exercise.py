import random


class CommandPrompt:

    def __init__(self, buy, sell, wait):
        self.buy = buy
        self.sell = sell
        self.wait = wait

    def ask(self):
        while True:
            answer = input("Decision [b/s/w/buy/sell/wait]:")
            if answer in self.buy:
                return 'buy'
            if answer in self.sell:
                return 'sell'
            if answer in self.wait:
                return 'wait'
            print(f'Invalid choice: {answer}')

class Wallet:

    def __init__(self, pln , usd):
        if type(pln) is not float or type(usd) is not float:
            raise ValueError

        self.pln = pln
        self.usd = usd

    def convert_pln_to_usd(self, rate):
        self.usd += self.pln/rate
        self.pln = 0

    def convert_usd_to_pln(self, rate):
        self.pln += self.usd*rate
        self.usd = 0


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


def main(usdpln_rates):
    wallet_pln = 100.0
    wallet_usd = 0.0
    wallet = Wallet(wallet_pln, wallet_usd)
    cp = CommandPrompt(["buy", 'b'], ['sell', 's'], ['wait', 'w', ''])
    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet.pln, 2)} PLN, ${round(wallet.usd, 2)}, rate {usdpln_rate}')
        choice = cp.ask()
        if choice in ('b', 'buy'):
            wallet.convert_pln_to_usd(usdpln_rate)
        elif choice in ('s', 'sell'):
            wallet.convert_usd_to_pln(usdpln_rate)
            wallet_usd = 0
    wallet_pln = wallet.pln
    wallet_pln += wallet.usd * usdpln_rate

    print(f'Your result: {wallet_pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)
