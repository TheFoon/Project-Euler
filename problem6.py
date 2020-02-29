square_of_sum = (sum(range(1, 101)))**2
sum_of_square = sum([x**2 for x in range(1, 101)])
result = abs(square_of_sum - sum_of_square)
print(result)