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

# 与えられた数の特性から全てが偶数か考えないといけない
def recursion(l: list, count: int):
    is_recurision = True
    for num in l:
        if num % 2 != 0:
            is_recurision = False
    if is_recurision:
        count += 1
        return recursion([n/2 for n in l], count)
    return count

n = int(input())
l = list(map(int, input().split()))
ans = recursion(l, 0)
print(ans)