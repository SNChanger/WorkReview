
import time

# 現在座標.
position_x = 0.0
position_y = -1500.0


# 移動するときのメインループ.
def main(position_x, position_y):
    # 速度
    # 動かすオブジェクトのスピードの基本値.
    object_default_speed = 150.0
    
    # 壁の末端まで移動して対応.
    wall_end_y_value = 3000.0

    # 計算用の最終速度.
    # 方角やブレーキの変更を再計算する 遅くなる土地だと  object_default_speed * 0.5
    velocity = object_default_speed
    
    print("wall check start")
    # 壁への移動処理.
    while True:
        position_y += velocity
        # 壁の末端に到達したら、終了する(ループする関数の処理で組み込む).
        if position_y > wall_end_y_value:
            print("wall hit app end")
            break
        print("now position y {0}".format(position_y))
        time.sleep(2)

    # 壁に当たったのでプログラムを終了.   
    print("wall check end")
        

# メイン処理を実行する.
main(position_x, position_y)



