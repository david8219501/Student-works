def id_id(numbers):
    for i in range(1,9):
        if i % 2 == 0:
            numbers[i] = int(numbers[i] * 2)
        if int(numbers[i]) // 10 > 0:
            numbers[i] = int(number[0]) + int(number[1])
    for j in range(1,9):
        sum_id = sum_id + numbers[j]
    key = (10 - (sum_id % 10) % 10)
    if key != numbers[8]:
        return False
    else: return True

numbers = input('enter the id number' )
while len(numbers) < 9:
    numbers = (input('enter the id number' ))
if id_id(numbers):
    print('Yes, the ID you provided is valid')
else:
    print('Oops, the ID that the rainbow is invalid')

