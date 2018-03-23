# -*- encoding: utf-8 -*-
import datetime


def get_logs(string):
    if string and string[0] == '[':
        try:
            int(string[-2:])
            return string
        except ValueError:
            return None


def get_data(log):
    start = log.find('GET ')
    end = log.find(' ', start + 4)
    url = log[start + 4: end + 1]
    request_time = log[log.rfind(' '):]
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    pos = url.find('?')
    url = url[0: pos]
    return url, request_time


def parse(
    ignore_files=False,
    ignore_urls=[],
    start_at=None,
    stop_at=None,
    request_type=None,
    ignore_www=False,
    slow_queries=False
):
    '''
        ТУТ ДОЛЖЕН БЫТЬ ВАШ КОД
    '''
    return []

# parse()
