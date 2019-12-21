#Needs optimization, use backtracking
def wordBreak(s, wordList):
    res = []
    i = 0
    j = 1

    while i < j and j < len(s)+1:
        if s[i:j] in wordList:
            res.append(s[i:j])
            i = j
            j = j+1
        else:
            j = j+1

    return res

print(wordBreak("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
