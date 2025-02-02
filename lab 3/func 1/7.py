def num(numbers):
    for i in range(len(numbers)-1):
        if (numbers[i]==3) and (numbers[i+1]==3):
            return True
    return False
input_numbers = input( "number: ")
numbers = input_numbers.split()
numbers = [int(num) for num in numbers]
print(num(numbers))
