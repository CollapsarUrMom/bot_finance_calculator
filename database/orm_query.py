import json


def parse():
    with open('D:\\Alex\\Python\\bot_finance_calculator\\Check12.json', mode= 'r', encoding= 'UTF-8') as data:
        j = json.load(data)
        print(j)

parse()