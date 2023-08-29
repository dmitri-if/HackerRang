if __name__ == '__main__':
    n = int(input())
    strok = ''
    count = 1
    for i in range(n):
        strok = strok + str(count)
        count += 1
    print(strok)
