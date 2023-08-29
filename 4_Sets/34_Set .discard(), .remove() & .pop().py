n = int(input())
s = set(map(int, input().split()))
n2=int(input())
for i in range(n2):
    command=list(input().split())
    if command[0]=='pop':
        s.pop()
    elif command[0]=='remove':
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))

total=0
for item in s:
    total=total + item
print(total)


# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5