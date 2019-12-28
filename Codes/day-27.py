def isBalanced(s):
    res = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            res.append(s[i])
            continue
        
        if len(res) == 0:
            return False

        if s[i] == ')':
            x = res.pop()
            if x in ['{', '[']:
                return False
        
        elif s[i] == '}':
            x = res.pop()
            if x in ['(', '[']:
                return False
        
        elif s[i] == ']':
            x = res.pop()
            if x in ['{', '(']:
                return False
    
    return len(res) == 0
        


print(isBalanced('([)]'))