from math import floor


class Coffee:
    water_cup = 200
    milk_cup = 50
    cof_beans_cup = 15

    def __init__(self, water, milk, beans, price):
        # super().__init__()
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price
        self.cups = 1

    def ingredients_amount(self):
        print(f'For {self.cups} cups of coffee you will need: \n'
              f'{self.water_cup * self.cups} ml of water\n'
              f'{self.milk_cup * self.cups} ml of milk\n'
              f'{self.cof_beans_cup * self.cups} g of coffee beans')

    def how_many_cups_can_be_made(self):
        water_needed = self.water_cup * self.cups
        milk_needed = self.milk_cup * self.cups
        cof_beans_needed = self.cof_beans_cup * self.cups

        if (self.water >= water_needed
                and self.milk >= milk_needed
                and self.beans >= cof_beans_needed):
            water_left = self.water - water_needed
            milk_left = self.milk - milk_needed
            cof_beans_left = self.beans - cof_beans_needed

            if (water_left >= self.water_cup
                    and milk_left >= self.milk_cup
                    and cof_beans_left >= self.cof_beans_cup):
                cups_made = self.remaining_cups_amount(water_left, milk_left, cof_beans_left)
                more_positive_msg = f'Yes, I can make that amount of coffee (and even {cups_made} more than that)'
                print(more_positive_msg)
            else:
                positive_msg = 'Yes, I can make that amount of coffee'
                print(positive_msg)
        else:
            cups_made = self.remaining_cups_amount(self.water, self.milk, self.beans)
            neg_msg = f'No, I can make only {cups_made} cups of coffee'
            print(neg_msg)

    def remaining_cups_amount(self, water_val, milk_val, cof_b):
        water_rem = water_val / self.water_cup
        milk_rem = milk_val / self.milk_cup
        cof_beans_rem = cof_b / self.cof_beans_cup

        cup_lst_am = [water_rem, milk_rem, cof_beans_rem]
        return floor(min(cup_lst_am))


class CoffeeMachine:
    def __init__(self, cups_am, water_am, milk_am, beans_am, cash_am):
        self.water_am = water_am
        self.milk_am = milk_am
        self.cof_beans_am = beans_am
        self.cups = cups_am
        self.cash_am = cash_am

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


mach_cups = 9
mach_water = 400
mach_milk = 540
mach_beans = 120
mach_cash = 550

coffee = CoffeeMachine(mach_cups, mach_water,
                       mach_milk, mach_beans, mach_cash)

while True:
    action_input = input('Write action (buy, fill, take, remaining, exit):\n')
    print()
    if action_input == 'buy':
        coffee_num = input(
            'What do you want to buy? 1 - espresso, 2 - latte, '
            '3 - cappuccino, back - to main menu:\n')
        if coffee_num != 'back':
            coffee_num = int(coffee_num)
        if coffee_num == 1:
            coffee.resource_check_prior_buying(250, 0, 16, 4)
            print()
        elif coffee_num == 2:
            coffee.resource_check_prior_buying(350, 75, 20, 7)
            print()
        elif coffee_num == 3:
            coffee.resource_check_prior_buying(200, 100, 12, 6)
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
        coffee.refill(water_fill_ml, milk_fill_ml,
                      beans_fill_gr, cups_fill_val)

    elif action_input == 'take':
        coffee.take()

    elif action_input == 'remaining':
        coffee.coffee_machine_status()
    elif action_input == 'exit':
        break
