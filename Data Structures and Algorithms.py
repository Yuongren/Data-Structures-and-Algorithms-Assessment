# Question 1
def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack


# Question 2
def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Question 3
import string

def word_frequency(sentence):
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator).lower()

    
    words = sentence.split()

    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict