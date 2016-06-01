
def quicksort(A, lo, hi):
    if len(A) <= 1:
        return A

    if lo < hi:
        mid = partition(A, lo, hi)
        quicksort(A, lo, mid-1)
        quicksort(A, mid+1, hi)
    
    return A


def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in  range(lo, hi):
        if A[j] <= A[hi]:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[hi] = A[hi], A[i]

    print(A)
    return i 


if __name__ == "__main__":
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    print(quicksort(a, 0, len(a)-1))
