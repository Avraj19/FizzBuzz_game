def check_3(num):
    return num % 3 == 0


def check_5(num):
    return num % 5 == 0


def check_15(num):
    return num % 15 == 0


while True:

    user_num = int(input('Enter number you want to play till: '))
    count_num = 1
    while user_num >= count_num:
        if check_15(count_num):
            print('FizzBuzz')
        elif check_5(count_num):
            print('Buzz')
        elif check_3(count_num):
            print('Fizz')
        else:
            print(count_num)
        count_num = count_num + 1
    user = str(input('Do you want to keep play FizzBuzz? y or exit ').lower().strip())
    if user == 'exit':
        print('See you next time.')
        break
