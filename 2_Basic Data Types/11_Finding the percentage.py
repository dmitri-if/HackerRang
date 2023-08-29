if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = list(student_marks[query_name])
    num = len(l)
    sum_of_all = sum(l)
    avarage = sum_of_all/num
    print(format(avarage, '.2f'))
