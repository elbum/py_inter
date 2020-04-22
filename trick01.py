dictionary = {"a": 1, "b": 2 , "c":3}
def someFunction(a, b):
    print(a + b)
    return
# these do the same thing:
someFunction(**dictionary)
someFunction(a=1, b=2)
