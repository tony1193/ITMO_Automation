def task_1() -> str:
    a: int = 4
    b: float = 8.15
    c: str = двадцать три'
    d: list = [1, 10, 100]
    e: bool = 15>7
    print(a, 'относится к типу', type(a))
    print(b, 'относится к типу', type(b))
    print(c, 'относится к типу', type(c))
    print(d, 'относится к типу', type(d))
    print(e, 'относится к типу', type(e))
task_1()


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    # ряд Фибоначчи
    return a[0:3]
print(task_2())

def task_3() -> int:
    a: int = 3
    return a ** 2
print(task_3())

