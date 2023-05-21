from math import floor


class CoffeeMachine:
    water_cup = 200
    milk_cup = 50
    cof_beans_cup = 15

    def __init__(self, cups, water, milk, beans):
        self.cups = cups
        self.water_am = water
        self.milk_am = milk
        self.cof_beans_am = beans

    def ingredients_amount(self):
        print(f'For {self.cups} cups of coffee you will need: \n'
              f'{self.water_cup * self.cups} ml of water\n'
              f'{self.milk_cup * self.cups} ml of milk\n'
              f'{self.cof_beans_cup * self.cups} g of coffee beans')

    def how_many_cups_can_be_made(self):
        water_needed = self.water_cup * self.cups
        milk_needed = self.milk_cup * self.cups
        cof_beans_needed = self.cof_beans_cup * self.cups

        if (self.water_am >= water_needed
                and self.milk_am >= milk_needed
                and self.cof_beans_am >= cof_beans_needed):
            water_left = self.water_am - water_needed
            milk_left = self.milk_am - milk_needed
            cof_beans_left = self.cof_beans_am - cof_beans_needed

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
            cups_made = self.remaining_cups_amount(self.water_am, self.milk_am, self.cof_beans_am)
            neg_msg = f'No, I can make only {cups_made} cups of coffee'
            print(neg_msg)

    def remaining_cups_amount(self, water, milk, cof_b):
        water_rem = water / self.water_cup
        milk_rem = milk / self.milk_cup
        cof_beans_rem = cof_b / self.cof_beans_cup

        cup_lst_am = [water_rem, milk_rem, cof_beans_rem]
        return floor(min(cup_lst_am))


water_amount = int(input('Write how many ml of water the coffee machine has:\n'))
milk_amount = int(input('Write how many ml of milk the coffee machine has:\n'))
cof_beans_amount = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
cups_amount = int(input('Write how many cups of coffee you will need:\n'))

coffee_machine_job = CoffeeMachine(cups_amount, water_amount,
                                   milk_amount, cof_beans_amount)

coffee_machine_job.how_many_cups_can_be_made()
