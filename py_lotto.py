def lotto():
    from random import randrange

    numbers = [0] * 41
    counter = 1
    lotto_num = ""

    while counter < 8:
        rand_num = randrange(1, 41)
        if numbers[rand_num] == 0:
            numbers[rand_num] = rand_num
            counter += 1
    for i in range(1, 41):
        if numbers[i] != 0:
            lotto_num = lotto_num + str(numbers[i]) + "  "
    return lotto_num


lines = int(input("Please enter number of lines: "))
while lines > 0:
    print(lotto())
    lines -= 1
