def textJustify(words, maxWidth):
    res, cur, num_of_letters = [], [], 0

    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    
    for i in range(maxWidth - num_of_letters):
        cur[i%(len(cur)-1 or 1)] += ' '
    res.append(''.join(cur))

    return res

res = textJustify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)

for row in res:
    print(row)