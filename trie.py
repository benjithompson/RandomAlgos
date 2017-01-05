#!/usr/bin/env python3

"""Trie example from HackerRank. First input is number of ops.
Add will insert given word. Find will return occurances of given substring"""

from collections import defaultdict

#Trie Node- data, # of subwords
class Trie(object):
    """Object to hold trie tree node data"""

    __slots__ = ['child', 'commonwords']

    def __init__(self):
        self.child = defaultdict(Trie)
        self.commonwords = 0

    def insert_word(self, word):
        """inserts letters of word into trie"""
        #print('inserting word: {0}'.format(word))
        node = self
        for letter in word:
            node = node.child[letter]
            node.commonWords = node.commonWords+1
            #print('{0},{1}'.format(letter, node.commonWords))
        node = node.child[None]

    def get_subwords(self, word):
        """returns number of words found with given substring"""

        node = self
        for letter in word:
            if letter not in node.child:
                return 0
            node = node.child[letter]
        return node.commonwords

N = int(input().strip())
trie = Trie() # #pylint: disable=invalid-name

for a0 in range(N):
    op, contact = input().strip().split(' ')
    #print('{0}: {1}'.format(op,contact))

    if op == 'add':
        trie.insert_word(contact)

    if op == 'find':
        count = trie.get_subwords(contact)
        print count
        