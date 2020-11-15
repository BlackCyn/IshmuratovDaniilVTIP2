#Сортировка выборкой
def selection(numbers):  
    # i = количеству отсортированных значений
    for i in range(len(numbers)):
        # Исходно считаем наименьшим первый элемент
        lowest = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[lowest]:
                lowest = j
        # меняем самый маленький элемент в списке на самый первый
        numbers[i], numbers[lowest] = numbers[lowest], numbers[i]

# Проверка
numb = [4, 2, 55, 123, 22]  
selection(numb)  
print("Массив, отсортированный выборкой", numb)



#Пузырьковая сортировка
def bubble(numbers):  
    # Присваиваем переменной switch, чтобы цикл запустился хотя бы один раз
    switch = True
    while switch:
        switch = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                # Меняем элементы 
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # Устанавливаем switch в True для следующей итерации
                switch = True

# Проверка
numb = [4, 2, 55, 123, 22]  
bubble(numb)  
print("Массив, отсортированный методом пузырька", numb)



#Сортировка вставками
def insertion(numbers):  
    for i in range(1, len(numbers)):
        item_to_insert = numbers[i]
        # Ссылку на индекс предыдущего элемента сохраняем
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше элемента для вставки
        while j >= 0 and numbers[j] > item_to_insert:
            numbers[j + 1] = numbers[j]
            j -= 1
        # Вставляем элемент
        numbers[j + 1] = item_to_insert

# Проверка
numb = [4, 2, 55, 123, 22]  
insertion(numb)  
print("Массив, отсортированный методом вставки", numb)



#Пирамидальная сортировка
def heapify(numbers, size, index):  
    # Индекс наибольшего элемента считаем корневым индексом
    largest = index
    left = (2 * index) + 1
    right = (2 * index) + 2

    if left < size and numbers[left] > numbers[largest]:
        largest = left

    if right < size and numbers[right] > numbers[largest]:
        largest = right

    if largest != index:
        numbers[index], numbers[largest] = numbers[largest], numbers[index]
        heapify(numbers, size, largest)

def heap_sort(nums):  
    n = len(nums)

    # Создаём Max Heap из списка
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

# Проверка
numb = [4, 2, 55, 123, 22]  
heap_sort(numb)  
print("Массива отсортированный пирамидальным методов", numb)



#Быстрая сортировка
def split(numbers, low, high):  
    # Cредний элемент выбираем в качестве опорного

    pivot = numbers[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while numbers[i] < pivot:
            i += 1

        j -= 1
        while numbers[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если левый от опорного элемента больше чем правый, меняем их местаими
        numbers[i], numbers[j] = numbers[j], numbers[i]

def quick1(numbers):  
    def quick2(items, low, high):
        if low < high:
            index = split(items, low, high)
            quick2(items, low, index)
            quick2(items, index + 1, high)

    quick2(numbers, 0, len(numbers) - 1)

# Проверка
numb = [4, 2, 55, 123, 22]  
quick1(numb)  
print("Массив, отсортированный методом быстрой сортировки", numb) 



#Сортировка методом слияния
def merge(left, right):  
    sorted = []
    left_index = right_index = 0

    left_length, right_length = len(left), len(right)

    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            # Сравниваем первые элементы в начале каждого списка

            if left[left_index] <= right[right_index]:
                sorted.append(left[left_index])
                left_index += 1
            else:
                sorted.append(right[right_index])
                right_index += 1

        elif left_index == left_length:
            sorted.append(right[right_index])
            right_index += 1

        elif right_index == right_length:
            sorted.append(left[left_index])
            left_index += 1

    return sorted

def merge_sort(numbers):  

    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)

# Проверка
numb = [4, 2, 55, 123, 22]  
numb = merge_sort(numb)  
print("Массив, отсортированный методом слияния", numb)




import math 
def my_sin (x,n):  
    x = x/180*math.pi 
    q = x
    s = 0 
    for i in range(1, n+1):
        s = s+ q
        q = q* (-1) * (x*x) / ((2*i+1) * (2*i)) 
    return s  





def f(x):
    return 2.718281828459045**(1+x)
def tailor(x, eps):
    x = 1+x
    sum = 1+x
    term = x;
    n = 2;
    while term*term > eps*eps:
        term *= x/n
        n += 1
        sum += term
    return sum

a=3.0
b=4.0
krok=(b-a)/10

while a<=b:    
    print(round(a,2), end=' ')
    print(round(f(a),5),end=' ')
    print(round(tailor(a,1e-6),5))
    a+=krok
