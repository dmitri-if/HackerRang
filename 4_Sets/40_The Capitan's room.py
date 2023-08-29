k=int(input())
rooms=list(map(int, input().split()))
a=set()
b=set()
for room in rooms:
    if room not in a:
        a.add(room)
        b.add(room)
    else:
        b.discard(room)
b=list(b)
print(b[0])


# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 