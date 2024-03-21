T = ("cc", "aa", "dd", "bb")
print(T)

tmp = list(T)  # convert tuple to list
tmp.sort()  # sort list
T = tuple(tmp)  # convert list to tuple
print(T)  # Prints ('aa', 'bb', 'cc', 'dd')
