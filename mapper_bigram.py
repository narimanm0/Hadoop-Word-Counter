#!/usr/bin/env python3
import sys
import re

# Load stopwords
stopwords = set()
with open('stopword_list.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.strip().lower()
        if word:
            stopwords.add(word)

# Process input from stdin
for line in sys.stdin:
    line = line.strip().lower()
    words = re.findall(r'\b[a-z]+\b', line)
    filtered_words = [w for w in words if w not in stopwords]
    
    # Generate bigrams
    for i in range(len(filtered_words) - 1):
        bigram = f"{filtered_words[i]} {filtered_words[i+1]}"
        print(f"{bigram}\t1")