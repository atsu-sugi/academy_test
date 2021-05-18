
okane = ('五千円','千　円','五百円','百　円','五十円','十　円','五　円','一　円')
okane2 = (5000,1000,500,100,50,10,5,1)
count = 0

# 各種金額入力
while True:
    konyu = input('購入金額:')
    nyukin = input('投入金額:')
    if int(konyu) > int(nyukin):
        print('投入金額が不足しています。')
        continue
    break

# お釣りを求める
otsuri = 0
otsuri = int(nyukin) - int(konyu)
print('お釣り:{}'.format(otsuri))

print('--------------------')

# 枚数計算
for i in okane2:
    print('{} : {}'.format(okane[count],otsuri // i))
    otsuri %= i
    count += 1




