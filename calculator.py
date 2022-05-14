from decimal    import Decimal
num1=input('Введите первое число: ')
num2=input('Введите второе число: ')
operation = input('Выберите операцию из следующих +-*/%**// ')
if num1.find('.')!=-1:
    num1=Decimal(num1)
else:
    num1=int(num1)
if num2.find('.')!=-1:
    num2=Decimal(num2)
else:
    num2=int(num2)
operation_list='+-*/%**//'
if operation_list.find(operation)==0:
    print(round(num1+num2, 2))
elif operation_list.find(operation)==1:
    print(round(num1-num2, 2))
elif operation_list.find(operation)==2:
    print(round(num1*num2, 2))
elif operation_list.find(operation)==3:
    print(round(num1/num2, 2))
elif operation_list.find(operation)==4:
    print(round(num1%num2, 2))
elif operation_list.find(operation)==5:
    print(round(num1**num2, 2))
elif operation_list.find(operation)==7:
    print(round(num1//num2, 2))
else:
    print('Данной операции нет в системе')