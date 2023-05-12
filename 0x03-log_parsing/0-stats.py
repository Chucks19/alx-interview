#!/usr/bin/python3

"""script reads stdin line by line and computes metrics """

import sys

cache_code = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
ttl_size = 0
counta = 0

try:
    for li in sys.stdin:
        li_list = li.split(" ")
        if len(li_list) > 4:
            cod = li_list[-2]
            siz = int(li_list[-1])
            if cod in cache_code.keys():
                cache_code[cod] += 1
            ttl_size += siz
            counta += 1

        if counta == 10:
            counta = 0
            print('File size: {}'.format(ttl_size))
            for key, value in sorted(cache_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(ttl_size))
    for key, value in sorted(cache_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
