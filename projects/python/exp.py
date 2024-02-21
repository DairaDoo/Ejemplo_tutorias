import random

list_of_numbers = []
ordered_list = []

for _ in range(10):
    list_of_numbers.append(random.randint(1, 1000))


for i in range(len(list_of_numbers)):
    if (list_of_numbers[i] + 1) < list_of_numbers[i]:
        print("Es menor!")
    elif (list_of_numbers[i] + 1) >= list_of_numbers[i]:
        print("Es mayor!")
     
 

print(list_of_numbers)
    
# for i in range(list_of_numbers):
#     print(list_of_numbers[i] - 1)