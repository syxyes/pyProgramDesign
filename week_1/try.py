Tem = input()
if Tem[0].lower() == 'f':
    C = (eval(Tem[1:-1]) - 32) / 1.8
    print('C{:.2f}'.format(C))
elif Tem[0].lower() == 'c':
    F = eval(Tem[1:-1]) * 1.8 + 32
    print('F{:.2f}'.format(F))

