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

N, Y = list(map(int, input().split()))
ans = "-1 -1 -1"
# 10,000円の数
for a in range(N+1):
    # 5,000円の数
    for b in range(N+1-a):
        c = N - a - b
        s = (10000*a) + (5000*b) + (c*1000)
        if s == Y:
            ans = "{} {} {}".format(a, b, c)
            break
print(ans)