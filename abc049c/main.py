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

S = input()
s = S[::-1]
org_s = S[::-1]

is_finish = False
t = ""


while is_finish is False:
    candidates = [
        "dream"[::-1],
        "dreamer"[::-1],
        "erase"[::-1],
        "eraser"[::-1]
    ]
    # 逆さまにして候補文字が挿入できそうなら行って残りの文字を次のループで判定する
    if s.startswith(candidates[0]):
        t += candidates[0]
        s = s.replace(candidates[0], "", 1)
    elif s.startswith(candidates[1]):
        t += candidates[1]
        s = s.replace(candidates[1], "", 1)
    elif s.startswith(candidates[2]):
        t += candidates[2]
        s = s.replace(candidates[2], "", 1)
    elif s.startswith(candidates[3]):
        t += candidates[3]
        s = s.replace(candidates[3], "", 1)
    else:
        is_finish = True

if org_s == t:
    print("YES")
else:
    print("NO")