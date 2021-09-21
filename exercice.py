#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2
    tax_rate = 0.15
    sum = 0
    for item in data:
        qty = item[INDEX_QUANTITY]
        price = item[INDEX_PRICE]
        sum += qty * price
    taxes = tax_rate * sum
    total = sum + taxes
    formated_bill = name
    # Solution sans répétition de code
    bill_lines = [
        ('SOUS TOTAL', sum),
        ('TAXES     ', taxes),
        ('TOTAL     ', total)
    ]
    for line in bill_lines:
        formated_bill += '\n' + f'{line[0]} {line[1]:>10.2f} $'
    # Solution avec répétition de code
    # formated_bill += '\n' + f'SOUS TOTAL {sum:>10.2f} $'
    # formated_bill += '\n' + f'TAXES      {taxes:>10.2f} $'
    # formated_bill += '\n' + f'TOTAL      {total:>10.2f} $'
    return formated_bill


def format_number(number, num_decimal_digits):
    return ""


def get_triangle(num_rows):
    border_char = '+'
    triangle_char = 'A'
    triangle_width = 1 + 2 * (num_rows - 1)
    border_row = (triangle_width + 2) * border_char

    result = border_row
    for i in range(num_rows):
        num_triangle_char = 1 + 2 * i
        result += '\n'
        result += border_char
        result += ' ' * ((triangle_width - num_triangle_char) // 2)
        result += triangle_char * num_triangle_char
        result += ' ' * ((triangle_width - num_triangle_char) // 2)
        result += border_char
    result += '\n' + border_row
    return result


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
