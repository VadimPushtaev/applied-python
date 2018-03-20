# -*- encoding: utf-8 -*-


def process(data, events, car):
    '''
        ТУТ ДОЛЖЕН БЫТЬ ВАШ КОД
    '''
    for train in data:
        print(train['name'])
        for car in train['cars']:
            print('\t{}'.format(car['name']))
            for man in car['people']:
                print('\t\t{}'.format(man))