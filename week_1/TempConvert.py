# TempConvert
TempStr = input("please input temperature with a symbol C/c or F/f: ")
if TempStr[-1].lower() == 'f':
    C = (eval(TempStr[0:-1]) - 32)/1.8 #不认识eval
    print('The converted temperature is {:.2f}C'.format(C)) #不知道format是干嘛的
elif TempStr[-1].lower() == 'c':
    F = 1.8*eval(TempStr[0:-1]) + 32
    print('The converted temperature is {:.2f}F'.format(F))
else:
    print('Wrong temperature format')

'''eval 负责'''
