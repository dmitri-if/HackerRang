def swap_case(s):
    x=''
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        x+=''.join(i)
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)