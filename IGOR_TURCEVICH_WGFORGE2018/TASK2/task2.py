#!/usr/bin/env python3
import sys

ERROR_CODE = 1


def get_text_from_file(path):
    from inspect import getsourcefile
    import os.path as op
    if not op.exists(path):
        dir = op.dirname(op.abspath(getsourcefile(lambda: 0)))
        path = op.join(dir, path)
        if not op.exists(path):
            raise FileNotFoundError(path)
    with open(path, 'r') as file:
        return file.read()


def get_ip_addresses_from_text(text):
    import re
    pattern = re.compile("([0-9]{1,3}[\.]){3}[0-9]{1,3}")
    return re.finditer(pattern, text)


def get_unique_ip_dict(ip_addresses):
    from collections import defaultdict
    ip_dict = defaultdict(lambda: 0)
    for match in ip_addresses:
        ip_dict[match.group(0)] += 1
    return ip_dict


def sort_ip_dict_by_count(ip_dict):
    return sorted(ip_dict.items(), key=lambda x: x[1])


def get_ip_address_by_frequency(ip_addresses, frequency_number):
    if frequency_number < 0:
        raise ValueError('Negative numbers are not allowed!')
    if frequency_number > len(ip_addresses):
        raise IndexError(
            'Bad number! There is only {} ip in text'.format(len(ip_addresses)))
    return ip_addresses[-int(frequency_number)][0]


def task2(path_to_file, frequency):
    text = get_text_from_file(path_to_file)
    result = analyze_text(text, frequency)
    print(result)


def analyze_text(text, frequency):
    ip_addresses = get_ip_addresses_from_text(text)
    unique_ip_dict = get_unique_ip_dict(ip_addresses)
    sorted_unique_ip_dict = sort_ip_dict_by_count(unique_ip_dict)
    ip_address = get_ip_address_by_frequency(sorted_unique_ip_dict,
                                             int(frequency))
    return ip_address


def main():
    if len(sys.argv) < 3:
        print('Usage: program path_to_file frequency_number')
        sys.exit(ERROR_CODE)
    task2(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
