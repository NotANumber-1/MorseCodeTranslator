import morse_code_core
while True:
    text = input("Text: ").upper()
    textlist = [i for i in text]
    morselist = []
    result = ""
    for i in textlist:
        try:
            morselist.append(morse_code_core.morse_dict[i]) 
        except:
            print(f"Unsupported letter: {i}")
    for i in morselist:
        result += f"{i} "
    print(result)