# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника)

n = int(input('Введите сколько долек у шоколадки по длинне: '))
m = int(input('Введите сколько долек у шоколадки по ширине: '))
k = int(input('Введите сколько долек отломить у шоколадки: '))
if k < m * n and (k % n == 0 or k % m == 0):
    print('Можно ровно отломить')
else:
    print('Нельзя ровно отломить')
if k == m * n:
	print('Ишь ты... Захотели целую шоколадку?')
if k > m * n:
	print('Так как шоколадка меньше чем вам хотелось!')