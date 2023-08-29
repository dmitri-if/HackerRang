if __name__ == "__main__":
    M = int(input().strip())
    set_m = set(map(int, input().strip().split(' ')))
    
    N = int(input().strip())
    set_n = set(map(int, input().strip().split(' ')))
    
    for j in sorted(set_m ^ set_n):
        print(j)

#     STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}