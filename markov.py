import random
import argparse
parser = argparse.ArgumentParser(description="Argparse")
"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = "In the quiet town, there was a small bakery, and in this bakery, the smell of fresh bread filled the air every morning. People would come from all around the town, drawn by the warm, comforting smell. The bakery owner, an older man with a friendly smile, greeted everyone who came in. Inside the bakery, shelves were filled with bread, pastries, and cakes, each one freshly baked and ready to enjoy. For the people of the town, the bakery was more than just a place to buy bread; it was a place to connect, to share a smile, and to start the day with something warm and comforting."
transitions = {}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""
words = text.split()
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""
def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    raw = " ".join(result) # All this ensures that the sentences start with a capitol letter
    raw = raw.split('.')
    raw = [raw.capitalize() for raw in raw]
    return ' '.join(raw)  # Returns the function


"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""
parser.add_argument("start", help="Starting word")  # Adds the starting word argument   
parser.add_argument("wordcount", help="Number of words to generate") # Adds the word count argument
args = parser.parse_args()
print(generate_text(args.start, int(args.wordcount))) # The actual output part itself
