# -*- encoding: utf-8 -*-

import json
from glob import glob

from passangers import process

error_message = 'ERROR in file {}. Expected: "{}", got: "{}"'


def run_tests():
    for filename in glob('tests/*.json'):
        data = json.load(open(filename))
        trains, events, result = data['trains'], data['events'], data['result']
        got = process(trains, events, result['car'])
        expected = result['amount']
        if got != expected:
            print(error_message.format(filename, expected, got))
            return
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
