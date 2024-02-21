import timeit

def sum_even_numers_for( numbers ):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

def sum_even_numbers_genexp(numbers):
    return sum( number for number in numbers if number % 2 == 0 )

numbers = list(range(1, 1001))

primer_tiempo = timeit.timeit(lambda: sum_even_numers_for(numbers), number = 100000)
print(f"Primer tiempo de ejecucíon {primer_tiempo:.2f}")

segundo_tiempo = timeit.timeit(lambda: sum_even_numbers_genexp(numbers), number = 100000)
print(f"Segundo tiempo de ejecucíon {segundo_tiempo:.2f}")

if primer_tiempo > segundo_tiempo:
    print(f"Primer tiempo es mayor con: {primer_tiempo} segundos")
else:
    print("El segundo tiempo es mayor")







    

    