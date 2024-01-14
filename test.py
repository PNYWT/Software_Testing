def find_frist(array,x):
    for count, value in enumerate(array):
        print("รอบที่ ",count)
        if value == x:
            return count
    return -1

abc = find_frist([1,1,1],2)
print(abc)