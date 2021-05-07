import morse_code_core
morse = input("Morse code: ")
morselist = morse.split(" ")
text = ""
for i in morselist:
    _ = morse_code_core.morse_dict_value.index(i)
    text += morse_code_core.morse_dict_key[_]
print(text.lower())

