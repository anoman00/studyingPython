
def numberoftimesStringAppearsInWord(string, word):
    num = 0
    for i in range(len(word)):
        if word[i:i+len(string)] == string:
            num +=1
    return('Number of times',string,' occurs is: '+str(num))