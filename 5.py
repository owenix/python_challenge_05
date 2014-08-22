#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5.py
#  

import pickle


junk = open('junk.p', 'rb')
data = pickle.load(junk)
junk.close()

for d in data:
    print("".join([e[1] * e[0] for e in d]))
