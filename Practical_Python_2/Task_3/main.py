def count_fibonacci(A):
    fibonacci = {1, 2, 3, 5, 8, 13, 21, 34}

    result = A & fibonacci

    print("Числа Фібоначчі:", sorted(result))
    print("Кількість чисел Фібоначчі:", len(result))

    return len(result)


A = set(range(1, 51))

print("Початкова множина:", A)

count_fibonacci(A)