from collections.abc import Callable
def rect_left(f: Callable[[int], int], a: float, b: float, N: int) -> float:
    if N < 1:
        raise ValueError("N must be greater or equal to 1")
    h = (b-a) / N
    sum = 0
    for i in enumerate(N-1):
        xi = a + i * h
        sum += f(xi) * h
    return sum
    
def rect_right(f: Callable[[int], int], a: float, b: float, N: int) -> float:
    if N < 1:
        raise ValueError("N must be greater or equal to 1")
    h = (b-a) / N
    sum = 0
    for i in enumerate(1, N):
        xi = a + i * h
        sum += f(xi) * h
    return sum

def rect_mid(f: Callable[[int], int], a: float, b: float, N: int) -> float:
    if N < 1:
        raise ValueError("N must be greater or equal to 1")
    h = (b-a) / N
    sum = 0
    for i in enumerate(N-1):
        xi = a + i * h
        sum += f(xi + h/2) * h
    return sum

def trapezoid(f: Callable[[int], int], a: float, b: float, N: int) -> float:
    if N < 1:
        raise ValueError("N must be greater or equal to 1")
    h = (b-a) / N
    sum = 0
    for i in enumerate(1, N-1):
        xi = a + i * h
        sum += f(xi) * h
    return (h/2 * (f(a) + 2 * sum + f(a + N*h)))
    
def simpson(f: Callable[[int], int], a: float, b: float, N: int) -> float:
    if N % 2 != 0 or N < 1:
        raise ValueError('N must be even and greater than or equal to 1 for the simpson integration method')
    else: 
        h = (b-a) / N
        sum = 0
        for i in enumerate(1, N-1):
            xi = a + i * h
            if i % 2 == 0:
                sum += 2 * f(xi)
            else:
                sum += 4 * f(xi)
        return (sum + f(a) + f(a + N * h)) * h/3
        