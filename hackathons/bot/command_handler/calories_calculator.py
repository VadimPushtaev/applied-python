import json
import re
from command_pool import CommandPool
from command_handler import CommandHandler


@CommandPool.register_command_class
class CaloriesCalculator(CommandHandler):
    def __init__(self):
        self.food_base = self.load_data()

    def handle(self, text):
        if text.startswith("calories_calc "):
            text = text.replace("calories_calc ", "").strip()
            commands = text.split(';')
            pattern = re.compile(r"(?P<name>[А-Яа-я ]*) ?-? ?(?P<weight>[\d,]*)")
            for command in commands:
                command_dict = pattern.match(command).groupdict()
                commands[commands.index(command)] = command_dict
            not_found_food = []
            found_food = {}
            for command in commands:
                params = self.food_base.get(command['name'].strip())
                if params:
                    if command['weight']:
                        found_food[command['name']] = {name: float(value) * float(command['weight'])/100 for name, value in params.items()}
                    else:
                        found_food[command['name']] = params
                else:
                    not_found_food.append(command['name'])
            results = []
            if not_found_food:
                for not_found in not_found_food:
                    results.append("Food '{}' is not found in base".format(not_found.strip()))
            if found_food:
                results.append("{:^30}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}"
                               .format('Продукт', 'Вода', 'Белки', 'Жиры', 'Углеводы', 'Калории'))
                results.append("_"*90)
                for name, parameter in found_food.items():
                    results.append("{:^30}|{:^10.2f}|{:^10.2f}|{:^10.2f}|{:^10.2f}|{:^10.2f}"
                                   .format(name, parameter['water'], parameter['proteins'], parameter['fats'], parameter['carbohydrates'], parameter['kcal']))
                    results.append("_" * 90)
            return '```' + '\n'.join(results) + '```'

    @staticmethod
    def load_data():
        with open("food_base.json", "r", encoding="utf8") as fb:
            return json.loads(fb.read())
