names = ['David', 'Helen', 'Anne']
lower_names = [i.lower() for i in names]
print(lower_names)  #> ['david', 'helen', 'anne']

even_numbers = [num for num in range(101) if num % 2 == 0]
print(even_numbers)

years = [1995, 2000, 2004, 2011]
leap_years = [years_i for years_i in years if years_i % 4 == 0]
print(leap_years)


def gen_odd_num(less_than):
    for x in range(less_than):
        if x % 2 == 1:
            yield x

for i in gen_odd_num(101):
	print(i)
