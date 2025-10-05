import re 
from collections import Counter
from textblob import TextBlob

with open("sample.txt", "r") as file:
    text = file.read()

def count_text(text):
    Words = text.split()
    Sentence = re.split(r'[.!?]', text)
    Paragraph = text.split("\n")
 
    Words_count= len(Words) 
    Sentence_count = len([s for s in Sentence if s.strip()!=''])
    Paragraph_count = len([p for p in Paragraph if p.strip()!=''])

    return Words_count, Sentence_count, Paragraph_count

def frequent_words(text, n=6):
    Words = re.findall(r'\w+', text.lower())
    counter = Counter(Words)

    return counter.most_common(n)


def time_taken(text, wpm=200):
    words = text.split()
    total_words = len(words)
    reading_time = total_words/wpm*60
    
    return round(reading_time)

Words_count, Sentence_count, Paragraph_count = count_text(text)
print("Words: ", Words_count)
print("Sentence: ", Sentence_count)
print("Paragraph: ", Paragraph_count)

print("Most frequent words: ", frequent_words(text))
print("Estimated time: ", time_taken(text), "seconds")
