# コインの金額
coinPriceList = [500, 100, 50, 10]

# 自動販売機内にあるコインの枚数
coinNumList = [20, 20, 20, 20]


def ProcessChangeCount():
    restChange = x - n
    # おつりのコインの枚数
    changeNumList = [0, 0, 0, 0]

    if restChange < 0:
        print("入金額が足りません")
        print()
        return

    for i in range(4):
        while (restChange - coinPriceList[i] >= 0) & (coinNumList[i] > 0):
            restChange -= coinPriceList[i]
            changeNumList[i] += 1
            coinNumList[i] -= 1

    if restChange == 0:
        print("購入完了")
        print("おつり:" + str(x - n) + "円")

        for i in range(4):
            if changeNumList[i] == 0:
                continue
            print(str(coinPriceList[i]) + "円:" + str(changeNumList[i]) + "枚")
    else:
        print("釣り切れのため購入できません")

    print()


while 1:
    n = int(input("商品の金額>"))
    x = int(input("入れた金額>"))
    print()

    ProcessChangeCount()
