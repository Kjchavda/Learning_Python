num = 910

print(f"{num:.4f}") #floating point precision
print(f"{num:10} test") #allocate spaces, if 10 are allocated then ther are 10-len(num) sapces before the number
print(f"{num:05}") #allocate spaces and zero pad, same logic as above
print(f"{num:<}") #left justify
print(f"{num:>}") # right justify
print(f"{num:^}") # center align    
#:, is used for seperating thousands
#can use .rjust .ljust and .center() methods
