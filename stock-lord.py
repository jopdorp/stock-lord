#!/usr/bin/env python3

from content import NEWS, MIRACLES, DISASTERS
import random


class FinancialGame:
    def __init__(self):
        self.cash = 10000
        self.ETI_units = 0  # European Tech Index
        self.EAI_units = 0  # European Automotive Index
        self.GHI_units = 0  # Global Healthcare Index
        self.EURUSD = 1.10  # Forex rate of EUR to USD
        self.days = 30  # Extendable
        self.news = NEWS
        self.miracles = MIRACLES
        self.disasters = DISASTERS
        self.exchanges = ["Amsterdam", "Frankfurt", "Paris", "London", "New York"]
        self.current_exchange = "Amsterdam"
        self.turns_left = 30
        self.previous_values = {"Amsterdam": {"ETI": 100, "GHI": 75},
                                "Frankfurt": {"EAI": 50, "EURUSD": 1.12},
                                "Paris": {"EAI": 50, "GHI": 75},
                                "London": {"ETI": 100, "EURUSD": 1.10},
                                "New York": {"ETI": 110, "EAI": 60, "GHI": 80, "EURUSD": 1.09}}
        self.stocks = {"ETI": ["Amsterdam", "London", "New York"],
                       "EAI": ["Frankfurt", "Paris", "New York"],
                       "GHI": ["Paris", "Amsterdam", "New York"]}
        self.forex = ["London", "Frankfurt", "New York"]
        
    def introduction(self):
        print("🎉🔥💰ATTENTION!!! Unleash the MILLIONAIRE within you!💰🔥🎉")
        print("\nDo YOU want to get RICH fast? Step right up! This is the once-in-a-lifetime chance you've been waiting for!")
        print("Welcome to the Financial Growth Simulator! Where dreams turn into CASH!")
        print("\nWant a yacht? A private jet? You can get it all! Just master these stocks:")
        print("1. ETI - European Tech Index: A goldmine conglomerate of the leading tech titans in Europe.")
        print("2. EAI - European Automotive Index: Drive your dreams with the top European automotive bigshots.")
        print("3. GHI - Global Healthcare Index: Cure your financial ailments with the powerhouses of healthcare.")
        print("\nBut wait, there's MORE! Dive into the glitzy world of Forex with EUR/USD and make money rain!")
        print("\nDon't wait! Dive in now and ride the wave of wealth! Let's begin!💰🚀🌟")
        
    def display_portfolio(self):
        print("\nYour portfolio:")
        print(f"Cash: €{self.cash:.2f}")
        print(f"ETI Units: {self.ETI_units:.2f}")
        print(f"EAI Units: {self.EAI_units:.2f}")
        print(f"GHI Units: {self.GHI_units:.2f}")
        print(f"EUR/USD Forex: €{self.cash/self.EURUSD:.2f}")
        print("")
   
    def play_game(self):
        for day in range(self.days):
            print(f"\nDay {day + 1}:")
            news_flash, asset, fluctuation, min_impact, max_impact = random.choice(self.news)
            self.news.remove((news_flash, asset, fluctuation, min_impact, max_impact))
            print(f"Newsflash: {news_flash}")

            daily_prices = {}  # Store the stock prices for this day
            for stock in self.stocks.keys():
                if self.current_exchange in self.stocks[stock]:
                    daily_prices[stock] = self.previous_values[self.current_exchange][stock] * random.uniform(min_impact, max_impact)
                    print(f"{stock}: €{daily_prices[stock]:.2f}/unit")

            print("")

            # Check if a miracle or disaster event occurs
            event_occurs = random.choice([True, False])
            if event_occurs:
                event_type = random.choice(['miracle', 'disaster'])
                event = random.choice(self.miracles) if event_type == 'miracle' else random.choice(self.disasters)
                event_name, stock, impact, _, _ = event
                
                if event_type == "miracle":
                    print("\n🌟Fantastic News! A Miraculous Event Just Transpired!🌟")
                else:
                    print("\n❗Breaking News! An Unexpected Catastrophe Strikes the Market!❗")
                
                print(f"Details: {event_name}")
                if stock == "EURUSD":
                    self.EURUSD *= impact  # Update the EURUSD value separately
                    print(f"{stock} value is now €{self.EURUSD:.2f}")
                else:
                    daily_prices[stock] *= impact  # Adjust the price due to the event
                    print(f"{stock} stock value on {self.current_exchange} market is now €{daily_prices[stock]:.2f}/unit")
            

            while True:
                print(f"\nYou are currently trading on the {self.current_exchange} exchange.")
                print("What would you like to do?")
                print("1. Buy units")
                print("2. Sell units")
                print("3. Switch markets")
                print("4. Do nothing")
                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    print("Which type of unit would you like to buy?")
                    available_stocks = [stock for stock in self.stocks.keys() if self.current_exchange in self.stocks[stock]]
                    for i, stock in enumerate(available_stocks):
                        print(f"{i+1}. {stock}")
                    stock_choice = input("Enter your choice: ")
                    try:
                        stock_choice = int(stock_choice)
                        if stock_choice < 1 or stock_choice > len(available_stocks):
                            raise ValueError
                    except ValueError:
                        print("Invalid choice. Please try again.")
                        continue
                    asset = available_stocks[stock_choice-1]
                    current_price = daily_prices[asset]
                    max_units_can_buy = self.cash / current_price
                    units = float(input(f"How many units of {asset} would you like to buy? (Max {max_units_can_buy:.2f} units) "))
                    if units > max_units_can_buy:
                        print(f"You cannot afford {units:.2f} units of {asset}. You can buy up to {max_units_can_buy:.2f} units.")
                        continue
                    cost = units * current_price
                    setattr(self, f"{asset}_units", getattr(self, f"{asset}_units") + units)
                    self.cash -= cost
                    print(f"You bought {units:.2f} units of {asset} on {self.current_exchange} market for €{cost:.2f}.")
                    print(f"Current price of {asset} on {self.current_exchange} market: €{current_price:.2f}/unit")

                elif choice == "2":
                    print("Which type of unit would you like to sell?")
                    available_stocks = [stock for stock in self.stocks.keys() if self.current_exchange in self.stocks[stock]]
                    for i, stock in enumerate(available_stocks):
                        print(f"{i+1}. {stock}")
                    stock_choice = input("Enter your choice: ")
                    try:
                        stock_choice = int(stock_choice)
                        if stock_choice < 1 or stock_choice > len(available_stocks):
                            raise ValueError
                    except ValueError:
                        print("Invalid choice. Please try again.")
                        continue
                    asset = available_stocks[stock_choice-1]
                    if getattr(self, f"{asset}_units") == 0:
                        print(f"You do not have any units of {asset} to sell.")
                        continue
                    current_price = daily_prices[asset]  # Use the stored price for this day
                    units = float(input(f"How many units of {asset} would you like to sell? "))
                    if units > getattr(self, f"{asset}_units"):
                        print(f"You do not have {units:.2f} units of {asset} to sell.")
                        print(f"You have {getattr(self, f'{asset}_units'):.2f} units of {asset} to sell.")
                        sell_all = input("Would you like to sell all your units instead? (y/n): ")
                        if sell_all.lower() == "y":
                            units = getattr(self, f"{asset}_units")
                        else:
                            continue
                    setattr(self, f"{asset}_units", getattr(self, f"{asset}_units") - units)
                    self.cash += units * current_price
                    print(f"You sold {units:.2f} units of {asset} on {self.current_exchange} market for €{units * current_price:.2f}.")
                    print(f"Current price of {asset} on {self.current_exchange} market: €{current_price:.2f}/unit")

                elif choice == "3":
                    if self.turns_left > 0:
                        available_exchanges = [exchange for exchange in self.exchanges if exchange != self.current_exchange]
                        print("Which exchange would you like to switch to?")
                        for i, exchange in enumerate(available_exchanges):
                            print(f"{i+1}. {exchange}")
                        exchange_choice = input("Enter your choice: ")
                        try:
                            exchange_choice = int(exchange_choice)
                            if exchange_choice < 1 or exchange_choice > len(available_exchanges):
                                raise ValueError
                        except ValueError:
                            print("Invalid exchange choice. Please try again.")
                            continue
                        self.current_exchange = available_exchanges[exchange_choice-1]
                        self.turns_left -= 1
                        print(f"You have switched to the {self.current_exchange} exchange. You have {self.turns_left} turns left to switch markets.")
                    else:
                        print("You have no turns left to switch markets.")

                elif choice == "4":
                    pass

                else:
                    print("Invalid choice. Please try again.")
                    continue

                break

            for stock in daily_prices:
                self.previous_values[self.current_exchange][stock] = daily_prices[stock]

            self.display_portfolio()

        print("\nEnd of simulation!")
        self.display_portfolio()
        print("Thank you for playing!")

if __name__ == "__main__":
    game = FinancialGame()
    game.introduction()
    game.play_game()