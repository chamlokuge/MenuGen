__author__ = 'PLNech'

import random

from utils.format import format_length_integer
from utils.config import Config
from utils.comparable import Comparable


class Dish(Comparable):
    def __init__(self, name=None, calories=None, fats=None, carbohydrates=None, proteins=None):
        self.max_calories = Config.parameters[Config.KEY_MAX_DISH_CALORIES]
        self.max_fats = Config.parameters[Config.KEY_MAX_DISH_FATS]
        self.max_carbohydrates = Config.parameters[Config.KEY_MAX_DISH_CARBOHYDRATES]
        self.max_proteins = Config.parameters[Config.KEY_MAX_DISH_PROTEINS]

        self.calories = calories if calories is not None else random.randint(0, self.max_calories)
        self.proteins = proteins if proteins is not None else random.randint(0, self.max_proteins)
        self.carbohydrates = carbohydrates if carbohydrates is not None else random.randint(0, self.max_carbohydrates)
        self.fats = fats if fats is not None else random.randint(0, self.max_fats)

        self.name = name if name is not None else Config.dish_names[random.randrange(0, len(Config.dish_names))]

    def __str__(self):
        format_name = "{:13s}"
        format_cal = "{:%i.1f} Cal" % format_length_integer(self.max_calories, 2)
        format_prot = "{:%i.2f} Prot" % format_length_integer(self.max_proteins, 3)
        format_carb = "{:%i.2f} Carb" % format_length_integer(self.max_carbohydrates, 3)
        format_fat = "{:%i.2f} Fat" % format_length_integer(self.max_fats, 3)
        format_all = "%s:%s,%s,%s,%s." % (format_name, format_cal, format_prot, format_carb, format_fat)

        return format_all.format(self.name, self.calories, self.proteins, self.carbohydrates, self.fats)

    def __repr__(self):
        return "Dish " + str(self)
