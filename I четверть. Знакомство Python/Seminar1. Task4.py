"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Примеры/Тесты:
3 2 4 -> yes
3 2 1 -> no
"""

n = 3
m = 2
piece = 1
if piece % n == 0 or piece % m == 0:
    print("yes")
else:
    print("no")