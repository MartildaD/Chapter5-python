number = 10

all_numbers = tuple(range(1, number +1))

def square(nums):
    return nums ** 2
squares = list(map(square, all_numbers))
print(squares)
