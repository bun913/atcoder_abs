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

N, A, B = list(map(int, input().split()))
ans = 0
for n in range(1, N+1):
    n_list = [int(s) for s in str(n)]
    _sum = sum(n_list)
    if _sum >= A and _sum <= B:
        ans += n
print(ans)
