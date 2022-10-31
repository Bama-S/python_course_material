#program that starts and ends with particular string
words = ["character","class","remark","channel", "miss"]
for word in words:
    if word.startswith("ch"):
        print("The word starts with ch in ", word)
    if word.endswith("ss"):
        print("The word ends with ss in ", word)
