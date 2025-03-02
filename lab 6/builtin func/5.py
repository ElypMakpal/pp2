# Write a Python program with builtin function that returns True if all elements of the tuple are true.

def all_elements_true(t):
    return all(t)


t1 = (True, True, True)
t2 = (True, False, True)

print(all_elements_true(t1))  
print(all_elements_true(t2))  
