#!/usr/bin/env python3
import sys
import re

# Load stopwords
stopwords = set()
with open('stopword_list.txt', 'r') as f:
    for word in f:
        stopwords.add(word.strip().lower())

for line in sys.stdin:
    words = re.findall(r'\b[a-z]+\b', line.lower())
    for word in words:
        if word not in stopwords:
            print(f"{word}\t1")
