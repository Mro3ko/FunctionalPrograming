text = "I completely agree with you"
result = list(map(lambda word: len(word), text.split()))

print(f"Text: {text}")
print(f"No. of letters in words: {result}")