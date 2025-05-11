#!/usr/bin/env python3

def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]
print(return_evens(list(range(1,100))))

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
sentence_list = ["Hello", "I'm doing great", "Python is fun"]
print(make_exclamation(sentence_list))