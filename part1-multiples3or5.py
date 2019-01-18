def multiples(num):
    total_set = set()
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total_set.add(i)
    return sum(list(total_set))

num = 1000
print(multiples(num))
