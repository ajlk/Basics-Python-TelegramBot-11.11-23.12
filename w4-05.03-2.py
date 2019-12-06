def n_po_k(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return n_po_k(n - 1, k) + n_po_k(n - 1, k - 1)


n, k = map(int, input().split())
print(n_po_k(n, k))
