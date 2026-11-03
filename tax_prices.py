prices = [100, 200, 300]

def tax(nums):
    return nums * 10/100
ten_percent_tax = list(map(tax, prices))
print(ten_percent_tax)
