dictionary = {"cat": "kanyau", "dog": "mbwa", "horse": "farasi"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "haiko kwa dictionary")
