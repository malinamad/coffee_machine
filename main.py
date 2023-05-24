class CoffeeMachine:
    def __init__(self):
        self.water_am = 400
        self.milk_am = 540
        self.cof_beans_am = 120
        self.cups = 9
        self.cash_am = 550

    def main(self):
        while True:
            action_input = input('Write action (buy, fill, take, remaining, exit):\n')
            print()
            if action_input == 'buy':
                coffee_num = input(
                    'What do you want to buy? 1 - espresso, 2 - latte, '
                    '3 - cappuccino, back - to main menu:\n')
                coffee_num = int(coffee_num) if coffee_num != 'back' else str()
                if coffee_num == 1:
                    self.resource_check_prior_buying(250, 0, 16, 4)
                    print()
                elif coffee_num == 2:
                    self.resource_check_prior_buying(350, 75, 20, 7)
                    print()
                elif coffee_num == 3:
                    self.resource_check_prior_buying(200, 100, 12, 6)
                    print()
                elif coffee_num == 'back':
                    continue

            elif action_input == 'fill':
                water_fill_ml = int(input('Write how many ml of water'
                                          'you want to add:\n'))
                milk_fill_ml = int(input('Write how many ml of milk '
                                         'you want to add:\n'))
                beans_fill_gr = int(input('Write how many grams of coffee beans '
                                          'you want to add:\n'))
                cups_fill_val = int(input('Write how many disposable cups '
                                          'you want to add:\n'))
                self.refill(water_fill_ml, milk_fill_ml,
                            beans_fill_gr, cups_fill_val)
            elif action_input == 'take':
                self.take()
            elif action_input == 'remaining':
                self.coffee_machine_status()
            elif action_input == 'exit':
                break

    def coffee_machine_status(self):
        print(f'The coffee machine has:\n'
              f'{self.water_am} ml of water\n'
              f'{self.milk_am} ml of milk\n'
              f'{self.cof_beans_am} g of coffee beans\n'
              f'{self.cups} disposable cups\n'
              f'${self.cash_am} of money\n')

    def refill(self, water, milk, beans, cups):
        self.water_am += water
        self.milk_am += milk
        self.cof_beans_am += beans
        self.cups += cups

    def buy(self, water, milk, beans, price):
        self.water_am -= water
        self.milk_am -= milk
        self.cof_beans_am -= beans
        self.cups -= 1
        self.cash_am += price

    def take(self):
        print(f'I gave you ${self.cash_am}')
        self.cash_am -= self.cash_am

    def resource_check_prior_buying(self, water, milk, beans, cups):
        if (water <= self.water_am
                and milk <= self.milk_am
                and beans <= self.cof_beans_am
                and cups <= self.cups):
            self.buy(water, milk, beans, cups)
            positive_msg = 'I have enough resources, making you a coffee!'
            print(positive_msg)
        else:
            neg_msg = 'No, I can make only cups of coffee'
            print(neg_msg)


if __name__ == '__main__':
    CoffeeMachine().main()
