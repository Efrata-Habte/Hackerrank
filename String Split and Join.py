def split_and_join(line):
    # write your code here
    res=line.split()
    ans="-".join(res)
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
