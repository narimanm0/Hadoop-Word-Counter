from collections import Counter

# Read word counts
word_counts = {}
result = "wordcount_sw_results.txt"
with open(result, "r") as f:
    for line in f:
        word, count = line.strip().split("\t")
        word_counts[word] = int(count)

# Calculate statistics
total_words = sum(word_counts.values())
unique_words = len(word_counts)
top10 = Counter(word_counts).most_common(10)

# Print nicely
print(f"Total words      : {total_words:,}")
print(f"Unique words     : {unique_words:,}")
print("\nTop 10 most frequent words:")
print(f"{'Word':<15}{'Count':>10}")
print("-" * 25)
for word, count in top10:
    print(f"{word:<15}{count:>10,}")
