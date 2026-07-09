import re

# Common English  stopwords
stopwords = { "i", "is", "the", "and", "a", "an", "in", "of", "to", "it", "this", "that"}

def clean_text(text):
    #Step 1: Lowercase
    text = text.lower()

    #Step 2: Remove URLs
    text = re.sub(r'https?://\S+', ' ', text)

    # Step 3: Remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Step 4: Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Step  5: Remove stopwords
    words = text.split()
    cleaned = [word for word in words if word not in stopwords]

    return " ".join(cleaned)

# Example usage
sample_text = "I LOVE NLP!!! Visit https://nlp.com for more info. Python is amazing in 2024!"

print("Before:", sample_text)
print("After :", clean_text(sample_text))