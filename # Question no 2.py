# story sting list 
story = input("Enter a story: ")

noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball"]

story = input("Enter a short story: ")

story_words = story.replace(".", "").replace(",", "").split()

found_nouns = []

for word in story_words:
    if word in noun_list:
        found_nouns.append(word)

print("Nouns found in the story:")
for noun in found_nouns:
    print(noun)
                                              
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

found_nouns = []
found_numbers = []

for word in words:
    if word in noun_list:
        found_nouns.append(word)
    elif word.isdigit():
        found_numbers.append(int(word))

found_nouns.append(found_numbers)

print("Final list (nouns with numbers as nested list):")
print(found_nouns)

print("Program Ended")
