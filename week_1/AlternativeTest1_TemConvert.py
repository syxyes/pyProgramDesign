Tem = input()
if Tem[-1].lower() == 'f':
    C = (eval(Tem[0:-1]) - 32) / 1.8
    print('{:.2f}C'.format(C))
elif Tem[-1].lower() == 'c':
    F = eval(Tem[0:-1]) * 1.8 + 32
    print('{:.2f}F'.format(F))
else:
    print('输入格式错误')


"C:\Users\Administrator\Anaconda3\python"
"c:\Users\Administrator\Anaconda3\python"