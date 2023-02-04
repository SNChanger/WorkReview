import random
def choise():


    # プレゼントを配る人の人数を設定
    first_group_number = 100
    second_group_number = 70
    third_group_number = 30

    # 配るのにかかった合計回数(ゲストごとのチャレンジでメモしたりする場合は利用)
    total_value = 0

    while True:

        # プレゼントは申し込まれた各グループ単位で抽選
        present_result = choise_present_group()
        total_value += 1
        print("{0} 回目のプレゼントを配るよ".format(total_value))

        # 抽選した場合は、一人にプレゼントを渡して人数を減らす
        if  0.0 < present_result and present_result < 1.0:
            print("1グループにプレゼントを配りました")
            first_group_number -= 1

        # グループ全員に配り終わって0になったら、抽選から除外
        if 1.0 < present_result and present_result < 2.0:
            print("2グループにプレゼントを配りました")
            second_group_number -= 1

        # 全員に配り終わったらプレゼントを完了にする
        if 2.0 < present_result and present_result < 3.0:
            print("3グループにプレゼントを配りました")
            third_group_number -= 1


        if 3.0 < present_result:
            print("外れだよ。")
            continue


        # 全員へのプレゼント配布判定.
        if is_present_end(first_group_number, second_group_number, third_group_number):
            break

    print("今回は {0}回で配り終わったよ。".format(total_value))

# プレゼントのループ完了処理用 中身の条件を変えたら、色々派生できる気がする.
def is_present_end(first_group_number, second_group_number, third_group_number):
    return first_group_number <= 0 and second_group_number <= 0 and third_group_number <= 0

# プレゼント配布時の最大数などの設定
def choise_present_group():
    return random.random()*4

print("プレゼントの配布を開始します")
# プレゼントを配る.
choise()

print("プレゼントの配布を終了します")
