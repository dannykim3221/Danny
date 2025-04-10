def read_single_digit(digit):
    digit_to_korean = '영일이삼사오육칠팔구'
    return digit_to_korean[int(digit)]

def read_number(number):
    result = ''
    if len(number) >= 1:
        result = result + read_single_digit(number[0])
    if len(number) >= 2:
        result = result + ' ' + read_single_digit(number[1])
    if len(number) == 3:
        result = result + ' ' + read_single_digit(number[2])

    return result

num = input('세 자리 정수 입력: ')
print(read_number(num))
