
import time

# キーボードの入力処理を取得する.
input_value = input("please auth number :")

print("input_result {0}".format(input_value))


score = 0

# 過去の特殊な人物は、補正をかけて開始する.
if "4000" in input_value:
    score += 2000

print("番号から推測するあなたのスコアは {0}".format(score))