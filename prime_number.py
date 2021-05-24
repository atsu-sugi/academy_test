#1 100未満の素数を列記する
# ※少しループの数が多いかも
limit = 100
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
