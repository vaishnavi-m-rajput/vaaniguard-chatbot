import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import json
import random

lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

def preprocess_intents():
    global words, classes, documents

    # Load intents from the JSON file
    with open('intents.json') as file:
        intents = json.load(file)

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Tokenize each word
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # Lemmatize, lowercase, remove duplicates
    words_cleaned = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
    words_cleaned = sorted(set(words_cleaned))
    classes = sorted(set(classes))

    training = []
    output_empty = [0] * len(classes)

    for doc in documents:
        bag = []
        word_patterns = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]
        for w in words_cleaned:
            bag.append(1 if w in word_patterns else 0)

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training, dtype=object)

    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    return words_cleaned, classes, train_x, train_y
