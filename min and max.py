numbers = [1,2,3,4,5,6,7,8,9,10,11]

min = numbers[0]
max = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]
print("min:",min)
print("max:",max)