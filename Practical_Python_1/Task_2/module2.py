def multiples_of_three():
    numbers = []

    for i in range(30, 61):
        if i % 3 == 0:
            numbers.append(i)

    return numbers