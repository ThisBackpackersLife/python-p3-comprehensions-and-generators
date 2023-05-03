#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = []
    for number in num_list:
        if number % 2 == 0:
            evens_list.append(number)
    return evens_list

def make_exclamation(sentence_list):
    new_list = [ i + "!" for i in sentence_list]
    return new_list

