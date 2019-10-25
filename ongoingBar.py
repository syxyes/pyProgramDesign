import time
print("Start".center(120, '-'))
start = time.perf_counter()
for i in range(0,101):
    a = '*' * i
    b = '-' * (101 - i)
    c = i
    dur = time.perf_counter() - start
    print('\r{:3}%[{}>{}] {:.2f}s'.format(c, a ,b, dur), end=(''))
print('\nEnd')