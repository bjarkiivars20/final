lis1 = [1,3,2,6,5,4,5,5,7,8,3]

hash_lis = []

for item in lis1:
    hash_lis.append(hash(item))

print(hash_lis)