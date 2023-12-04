def fibonacci(x):
    fiblist = [0, 1]  
    while fiblist[-1] < x:
        n = fiblist[-1] + fiblist[-2]
        fiblist.append(n)
    fiblist=fiblist[2::]
    return fiblist


def fibsys(x):
    fiblist = fibonacci(x)
    fibsystem = []

    for i in reversed(fiblist):
        if i <= x:
            fibsystem.append(1)
            x -= i
        else:
            fibsystem.append(0)

    return fibsystem


x = int(input("введите число: "))
fibsystem = fibsys(x)

print("представление в виде чисел Фиобоначи", x, ":")
for i in fibsystem:
    print(i, end=" ")
