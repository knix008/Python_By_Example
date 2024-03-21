# Common errors in tuple unpacking
# T = ("red", "green", "blue", "cyan")
# print(T)
# (a, b) = T
# Triggers ValueError: too many values to unpack

T = ("red", "green", "blue")
print(T)
(a, b, c, d) = T
# Triggers ValueError: not enough values to unpack (expected 4, got 3)
