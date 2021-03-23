#!/usr/bin/env python3
import sys

def make_errory(l):
    result = "\033[01m\033[91m"+l+"\033[00m\033[00m"
    return result

def make_successy(l):
    result = "\033[01m\033[92m"+l+"\033[00m\033[00m"
    return result

if len(sys.argv) < 2:
    print("Supply at least one country to check")
    sys.exit(1)

CLOSED_LETTERS="ABDOPQR"

for i in range(1, len(sys.argv)):
    country_test = sys.argv[i].upper()
    open = True
    result_string = " is open!!!"
    for cl in CLOSED_LETTERS:
        if country_test.find(cl) >= 0:
            open = False
            result_string = " is " + make_errory("closed")
            country_test = country_test.replace(cl, make_errory(cl))
    if open:
        print(make_successy(country_test + result_string))
    else:
        print(country_test + result_string)
