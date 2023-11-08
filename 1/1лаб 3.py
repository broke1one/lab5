number = input("Enter list of numbers: ")
number_list = [int(num) for num in number.split()]
result = 1
for i in range(len(number_list)):
    if i % 2 != 0:
        result *= number_list[i]
print(f"your list is {number_list}")
print(result)
max_element = max(number_list)
print (f"max element is {max_element}")
number_list.remove(max_element)
print(f"new list without max element is {number_list}")
number_list.sort()
print(number_list[-1:-4:-1])