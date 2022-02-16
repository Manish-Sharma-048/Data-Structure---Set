'''
Write a Python program to remove an item from a set if it is present in the set.
'''

st = {1,2,3,4,5,6}

key = int(input("Enter key: "))

if key in st:
    st.remove(key)
    print("Key is removed")
else:
    print("Key is not present")
