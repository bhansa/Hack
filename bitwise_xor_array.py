def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n -= 2
    if n % 8 == 0 or n % 8 == 1:
        return 2
    if n % 8 == 4 or n % 8 == 5:
        return 0
    if n % 8 == 2 or n % 8 == 3:
        return n + 4
    if n % 8 == 6 or n % 8 == 7:
        return n + 2
    assert False

q = int(input())
assert 1 <= q <= 10 ** 5
for i in range(q):
    l, r = map(int, raw_input().split(" "))
    assert 1 <= l <= r <= 10 ** 15
    print (f(r) ^ f(l - 1))