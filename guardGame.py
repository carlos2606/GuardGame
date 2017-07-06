def answer(x):
    l = []
    s = 0
    for digits in str(x):
        l.append(int(digits))
    while len(l) != 1:
        s += l[0] + l[1]
        if len(str(s)) == 1:
            l[0] = s
            l.remove(l[1])
        else:
            l[0] = int(str(s)[0])
            l[1] = int(str(s)[1])
        s = 0
    return l[0]

def get_number():
    x = int(input("Enter a number: "))
    if x >= 0 and x < 2**31-1 :
        y = answer(x)
        print (y)
    else:
        print("Number should be be 0 or greater and less than 2147483647")


get_number()

