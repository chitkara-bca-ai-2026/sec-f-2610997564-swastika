# Text Processing Tool

print("========================================")
print("          TEXT PROCESSING TOOL")
print("========================================")

sentence = input("Enter a sentence: ")

print("--- Processing Results ---")

position = int(input("Enter position for indexing: "))

print("Character at position", position, ":", sentence[position])

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))

print("Sliced string [" + str(start) + ":" + str(end) + "] :", sentence[start:end])

print("Uppercase :", sentence.upper())
print("Lowercase :", sentence.lower())

old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")

new_sentence = sentence.replace(old_word, new_word)

print("After replace :", new_sentence)

print("Length of sentence :", len(sentence))

print("========================================")
print("Analysis Complete!")
print("========================================")