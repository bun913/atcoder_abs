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

N = int(input())
l = list(map(int, input().split()))
_sorted = sorted(l, reverse=True)
alice = 0
bob = 0
for i, n in enumerate(_sorted):
    is_alice = i % 2 == 0
    if is_alice:
        alice += n
    else:
        bob += n
print(alice-bob)
