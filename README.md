# We receive a sentence from the user
# We find the number of vowels, consonants and spaces in this sentence.
# We find the word and letter that occurs most often in the sentence.

from collections import Counter

text = input("Please enter the text: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
consonants =  "bcdfghjklmnpqrstvwxyz"

def analyze_text():
    
     vowel_counter = 0
     consonant_counter = 0
     space_counter = 0
     letters = set()
     
     for ch in text:
        if ch in vowels:
            vowel_counter += 1
            letters.add(ch)
        elif ch in consonants:
            consonant_counter += 1
            letters.add(ch)
        elif ch == " ":
            space_counter += 1
        elif ch in vowels or ch in consonants:
            letters.add(ch)
            
# Most repeated letter

     letter_counts = Counter([c for c in text if c in alphabet])
     most_common_letter, freq_letter = letter_counts.most_common(1)[0]
     
# The most repeated word

     word_counts = Counter(text.split())
     most_common_word, freq_word = word_counts.most_common(1)[0]
     
     return f"""
    Vowels: {vowel_counter}
    Consonants: {consonant_counter}
    Spaces: {space_counter} 
    Most common letter: '{most_common_letter}' ({freq_letter} times) 
    Most common word: '{most_common_word}' ({freq_word} times) 
    Letters found:{','.join(sorted(letters))}   
    """

print(analyze_text())
