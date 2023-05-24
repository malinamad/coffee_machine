from math import floor


# it was created as first stages and no longer in use in the main code
class Coffee:
    water_cup = 200
    milk_cup = 50
    cof_beans_cup = 15

    def __init__(self, water, milk, beans, price):
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
