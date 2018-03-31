# -*- encoding: utf-8 -*-

import json
from glob import glob
from log_parse import parse

error_message = 'Ошибка в файле {}. Expected: "{}", got: "{}"'


def run_tests():
    for filename in glob('tests/*.json'):
        data = json.load(open(filename))
        params, response = data['params'], data['response']
        got = parse(**data['params'])
        for index, item in enumerate(response):
            if len(got) != len(response) or got[index] != response[index]:
                print("Полученный и ожидаемый массивы различаются, получен: {} ожидался: {}, файл {}".format(
                    str(got), str(response), filename
                ))
                return
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
