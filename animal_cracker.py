def animal_cracker(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
