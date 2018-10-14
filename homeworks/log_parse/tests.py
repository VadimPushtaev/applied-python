# -*- encoding: utf-8 -*-

import json
from glob import glob
from log_parse import parse

error_message = "Полученный и ожидаемый массивы различаются, получен: {} ожидался: {}, файл {}"


def run_tests():
    for filename in glob('tests/*.json'):
        data = json.load(open(filename))
        params, response = data['params'], data['response']
        got = parse(**params)
        if len(got) != len(response):
            print(error_message.format(
                str(got), str(response), filename
            ))
        for index, item in enumerate(response):
            if got[index] != response[index]:
                print(error_message.format(
                    str(got), str(response), filename
                ))
                return
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
