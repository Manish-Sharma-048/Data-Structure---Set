'''
Write a Python program to create a symmetric difference. 
'''

s1 = {1,2,3}
s2 = {3,4,5}

cp = s1.intersection(s2)
s3 = s1.union(s2)
s3 = s3.difference(cp)

print(s3)
