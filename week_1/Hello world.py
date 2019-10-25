num = input('please tell me a number: ')
num = int(num)
if num == 0:
    print('Hello World')
elif num > 0:
    print('He' + '\nll' + '\no ' + '\nWo' + '\nrl' + '\nd')
else:
    for word in 'Hello World':
        print(word)