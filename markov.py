#!/usr/bin/env python

import random
import time
import os
import re
import twitter # from https://github.com/bear/python-twitter
import twittersecrets # contains keys and secrets

# NEEDED:
# rudeman.txt
# twittersecrets.py


def style_dict(filename):
    """Returns style_dict mapping each word to list of words which follow it.
        Args:filename
        Returns: dictionary of words with potential followings words
    """
    f = open(filename, 'r')
    tekst = f.read().split()
    word_dict = {}
    word_dict[''] = [tekst[0]]
    for i in range(len(tekst)-1):
        w = tekst[i]
        if w[0] == '>':
            word_dict[''].append(w[1:])
        else:
            if w in word_dict.keys():
                word_dict[w].append(tekst[i+1])
            else:
                word_dict[w] = [tekst[i+1]]        

    return word_dict


def print_speech(style_dict, word):
    """Given style_dict and start word, prints 100 random words.
        Args: Dictionary
        Returns: prints to screen
    """
    text = []
    for i in range(100):
        if not word in style_dict.keys():
            word = ''
        new_word = random.choice(style_dict[word])
        text.append(new_word)
        word = new_word
    return text


def main():
    """Rudeman-generator: Mimics style of Rudeman's forum posts.
        Args: void
        Returns : none
    """
    dict = style_dict('rudeman.txt')

    api = twitter.Api(consumer_key          = twittersecrets.CONSUMER_KEY,
                      consumer_secret       = twittersecrets.CONSUMER_SECRET,
                      access_token_key      = twittersecrets.ACCESS_KEY,
                      access_token_secret   = twittersecrets.ACCESS_SECRET)

    while True: 

        to_print = print_speech(dict, '') #Start from empty string
        charlist = []
        for w in to_print:
            for c in w:
                charlist.append(c)
            charlist.append(' ')
            if len(charlist) > 140:
                break

        i = 140
        interpunction = False
        while not interpunction and i > 0:
            i -= 1
            if charlist[i] in ['"','.','!','?']:
                interpunction = True

        if i > 20:
            tweet = ''.join(charlist[:i+1])
            api.PostUpdate(tweet)
            print tweet
            t = time.clock()
            period = 43200
            while True:
                if (time.clock() - t > period):
                    break


if __name__ == "__main__":
    main()