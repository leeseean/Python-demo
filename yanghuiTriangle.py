# Python杨辉三角实现
def yanghuiTriangle():
    L = [1]
    while True:
        yield L
        L = [1]+[L[x-1]+L[x] for x in range(1,len(L))]+[1]
for item in yanghuiTriangle():
    print(item)
    if len(item)>10:
        break

