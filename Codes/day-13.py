def longest_substr_with_k_distinct_char(s, k):
    if k == 0:
        return 0
    
    bound = (0, 0)
    max_len = 0
    h = {}

    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bound[0]
        else:
            char_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(char_to_pop) + 1
        
        bound = (new_lower_bound, bound[1]+1)
        max_len = max(max_len, bound[1]-bound[0])
    
    return max_len

print(longest_substr_with_k_distinct_char('abcba', 2))