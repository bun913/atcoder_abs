"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input() 
#int型で受け取るとき
s = int(input()) 
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
import sys

# 時間に対して手数が足りない
def is_too_far(abs_t, abs_dis):
    return abs_dis > abs_t

# 距離は圏内だが偶奇的に辿り着けない場合
# 距離と時間の偶数奇数が一致する場合はTrue
def is_can_reach(abs_t, abs_dis):
    is_even_abs = abs_t % 2 == 0
    is_even_dis = abs_dis % 2 == 0
    return is_even_abs == is_even_dis
    # if is_even_abs is True and is_even_dis is True:
    #     return False
    # if is_even_abs is False and is_even_dis is False:
    #     return False
    # return True

# 初期位置
p_x = 0
p_y = 0
p_t = 0
n = int(input())

# n回文繰り返す
for n in range(n):
    t, x, y = list(map(int, input().split()))
    # tの差から手数を求める
    abs_t = t - p_t
    # xとyの差から絶対距離を求める
    dis = abs(x - p_x) + abs(y - p_y)
    too_far = is_too_far(abs_t, dis)
    can_reach = is_can_reach(abs_t, dis)
    # print("abs_t: {}, abs_dis: {}".format(abs_t, dis))
    if (too_far is True or can_reach is False):
        # print("#####################")
        # print("x:{}, y:{}, ,t: {}".format(x,y,t))
        # print("#####################")
        print("No")
        sys.exit()
    p_x = x
    p_y = y
    p_t = t

print("Yes")