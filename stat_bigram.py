from collections import Counter

bigram_counts = {}

with open("wordcount_bigram_results.txt", "r") as f:
    for line in f:
        bigram, count = line.strip().split("\t")
        bigram_counts[bigram] = int(count)

top10_bigrams = Counter(bigram_counts).most_common(10)

total_bigrams = sum(bigram_counts.values())
unique_bigrams = len(bigram_counts)

print("Total bigrams       :", total_bigrams)
print("Unique bigrams      :", unique_bigrams)
print("\nTop 10 most frequent bigrams:")
print("{:<20} {:>6}".format("Bigram", "Count"))
print("-" * 28)
for bigram, count in top10_bigrams:
    print("{:<20} {:>6}".format(bigram, count))
