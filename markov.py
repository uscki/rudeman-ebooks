#!/usr/bin/env python

# Authors: Sjoerd Dost and Benno Kruit

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
    rawtekst = f.read().split()
    tekst = []
    for word in rawtekst:
        # Split op interpunctie
        if not word[:4] == "http":
            m = re.match('(.*)([.,?!\)\(])(.*)', word)
            if m:
                tekst.extend([x for x in list(m.groups()) if not x == ''])
            else:
                tekst.append(word)
        else:
            tekst.append(word)

    word_dict = {}
    word_dict[''] = [tekst[0][1:]]
    for i in range(len(tekst)-1):
        w = tekst[i]
        # '>' indicates start of forum post, needs to be stripped off.
        # also, as a possible starting word, map to ''
        if w[0] == '>':
            w = w[1:]
        next = tekst[i+1]
        parentheses = ['(',')']
        if not next in parentheses and not w in parentheses:
            if next[0] == '>':
                next = next[1:]
                word_dict[''].append(next)
            if w in word_dict.keys():
                word_dict[w].append(next)
            else:
                word_dict[w] = [next]   

    return word_dict


def generate_words(style_dict, word):
    """Given style_dict and start word, generate 100 words via markov chain.
        Args: Dictionary
        Returns: List of words
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
        Twitters as @rudeman_ebooks
        Args: void
        Returns : none
    """
    dict = style_dict('rudeman.txt')

    api = twitter.Api(consumer_key          = twittersecrets.CONSUMER_KEY,
                      consumer_secret       = twittersecrets.CONSUMER_SECRET,
                      access_token_key      = twittersecrets.ACCESS_KEY,
                      access_token_secret   = twittersecrets.ACCESS_SECRET)


    punct = ['"','.','!','?']

    # Twitter each 12 hours
    while True: 

        # Generate a list of words
        to_print = generate_words(dict, '') #Start from empty string

        charlist = []
        for i, w in enumerate(to_print):
            for c in w:
                charlist.append(c)
            if i < len(to_print) and not to_print[i+1] in punct:
                charlist.append(' ')
            if len(charlist) > 140:
                break

        # Take less than 140 characters, stopping at the last interpunction
        i = 140
        interpunction = False
        while not interpunction and i > 0:
            i -= 1
            if charlist[i] in punct:
                interpunction = True

        # If the tweet is sizable enough, tweet it, and count 12 hours.
        if i > 20:
            tweet = ''.join(charlist[:i+1])
            api.PostUpdate(tweet)
            print '-----------------------------------------------'
            print tweet
            t = time.clock()
            period = 43200
            while True:
                if (time.clock() - t > period):
                    break


if __name__ == "__main__":
    main()