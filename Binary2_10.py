L = []
import sys

# 2進数入力
binary = input('2進数:')
for i in binary:
    L.insert(0, i)
    if int(i) > 1:
        print('1か0で入力してください。')
        sys.exit(1)

# 計算
count = 0
binary2 = 1
decimal = 0
while count < len(binary):
    if int(L[count]) == 1:
        decimal += binary2
    count += 1
    binary2 *= 2

# 表示
print('10進数:{}'.format(decimal))