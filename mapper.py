#!/usr/bin/env python3
import sys
import re

# Read from standard input
for line in sys.stdin:
    # Convert to lowercase for the cases of capital letter
    line = line.strip().lower()
    # Tokenize using regex to keep only words
    words = re.findall(r'\b[a-z]+\b', line)
    for word in words:
        print(f"{word}\t1")
