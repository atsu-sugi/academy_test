count = 1
while True:
    if count % 3 == 0:
        if count % 5 == 0:
            print('FizzBuzz')
            count += 1
        else:
            print('Fizz')
            count += 1
    elif count % 5 == 0:
        print('Buzz')
    if count > 100:
        break
    print(count)
    count += 1