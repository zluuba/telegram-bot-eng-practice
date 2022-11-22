#!/usr/bin/env python3

def greet_user():
    dictionary = {"greeting": 'hello', "what": 'world'}

    result = ', '.join(map(str, list(dictionary.values())))
    return result

print(greet_user())
