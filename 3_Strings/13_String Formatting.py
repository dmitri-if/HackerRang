def print_formatted(number):
    # your code goes here
    for i in range(1,n+1):
        if len(bin(i)[2:]) >=2:
            print('', i,'', oct(i)[2:], '', hex(i)[2:].upper(), bin(i)[2:])
        else:
            print('', i,'', oct(i)[2:], '', hex(i)[2:], '', bin(i)[2:])   
        i+=1
        

if __name__ == '__main__':
    n = int(input())    #17
    print_formatted(n)