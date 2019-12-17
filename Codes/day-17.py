def longestDirPath(s):
    items = s.split('\n')
    dir_path = []
    max_len = 0

    for item in items:
        depth = item.count('\t')
        if '.' not in item:
            if depth >= len(dir_path):
                dir_path.append(item.strip('\t'))
            else:
                dir_path[depth] = item.strip('\t')
        else:
            max_len = max(max_len, len('\\'.join(dir_path[:depth]+[item.strip('\t')])))
    
    return max_len

print(longestDirPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'))