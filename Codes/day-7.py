#Recursive Solution
def helper(data, k):
    if k == 0:
        return 1
    #Starting index
    s = len(data) - k
    if data[s] == '0':
        return 0
    
    res = helper(data, k-1)

    if k >= 2 and int(data[s:s+2]) <= 26:
        res += helper(data, k-2)
    
    return res

def num_ways(data):
    return helper(data, len(data))

#DP Solution
def helper_dp(data, k, memo):
    if k == 0:
        return 1
    #Starting index
    s = len(data) - k
    if data[s] == '0':
        return 0
    
    if memo[k] != None:
        return memo[k]
    
    res = helper_dp(data, k-1, memo)

    if k >= 2 and int(data[s:s+2]) <= 26:
        res += helper_dp(data, k-2, memo)
    
    memo[k] = res

    return res

def num_ways_dp(data):
    memo = [None]*(len(data)+1)
    return helper_dp(data, len(data), memo)

string = '1233425343452343421233425343452343421233425343452233425343452233425343452'
print(num_ways_dp(string))