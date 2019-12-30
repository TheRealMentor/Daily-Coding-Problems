def encode(string):
    res = ''
    st = []

    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            st.append(string[i-1])
        else:
            st.append(string[i-1])
            res += str(len(st)) + st[-1]
            st = []

    #Corner case when last 2 alphabets are not same
    if string[-1] != string[-2]:
        res += '1' + string[-1]
    else:
        st.append(string[-1])
        res += str(len(st)) + st[-1]
    
    return res

print(encode('AAAABBBCCDAA'))

def decode(code):
    res = ''
    
    for i in range(0, len(code), 2):
        res += int(code[i])*code[i+1]
    
    return res

print(decode('3A2B1C'))
