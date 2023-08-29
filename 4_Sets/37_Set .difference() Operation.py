angl=int(input())
students_angl=list(map(int,input().split()))
franch=int(input())
students_franch=list(map(int,input().split()))
s=set(students_angl)
print(len(s.difference(students_franch)))


#input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8