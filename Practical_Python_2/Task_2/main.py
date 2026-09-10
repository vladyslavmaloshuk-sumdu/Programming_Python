def insert_after_element(A, element, new_element):
    index = A.index(element)
    A.insert(index + 1, new_element)
    return A


A = list(map(int, input("Введіть список: ").split()))

print("Початковий список:", A)

element = int(input("Введіть елемент, після якого потрібно вставити новий: "))
new_element = int(input("Введіть новий елемент: "))

if element in A:
    result = insert_after_element(A, element, new_element)
    print("Результат:", result)
else:
    print("Зазначеного елемента немає у списку.")