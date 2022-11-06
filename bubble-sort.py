
# スペース区切りで入力された複数の数字を並べ替え

def bubble_sort(data):
    length = len(data)
    # 右の要素のループ
    for r in range(1, length):
        # 左の要素のループ
        for l in range(0, length-1):
            # 隣り合う2つの要素を比較し、左が大きい場合は入れ替える
            if data[l] > data[l+1]:
                data[l], data[l+1] = data[l+1], data[l]

# 標準入力
DATA = [int(s) for s in input().split()]

bubble_sort(DATA)
print(DATA)