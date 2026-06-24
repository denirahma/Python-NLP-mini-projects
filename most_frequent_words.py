text = "I love learning NLP I love Python NLP is fun learning Python is amazing"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

    print("Word Fequency:")
    print(word_count)

    most_frequent = max(word_count, key=word_count.get)
    print(f"\nMost fequent word: '{most_frequent}' ({word_count[most_frequent]} times)")