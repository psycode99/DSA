def string_reversal(word: str):
    if len(word) in (0, 1):
        return word
    else:
        return string_reversal(word[1:]) + word[0] 
    
print(string_reversal("stella"))