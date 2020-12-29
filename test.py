def sort_algorithm(A):
    N = len(A)
    list_is_sorted = False
    bypass = 1
    while not list_is_sorted:
        list_is_sorted = True
        for k in range(N - bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                list_is_sorted = False
        bypass += 1


def test_sort():
    print("Test #1")
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    passed = A == A_sorted
    print("Ok" if passed else "Fail")

    print("testcase #2: ", end="")
    A = []
    A_sorted = []
    sort_algorithm(A)
    passed = A == A_sorted
    print("Ok" if passed else "Fail")

    print("testcase #3: ", end="")
    A = [1, 2, 3, 4, 5]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    passed = A == A_sorted
    print("Ok" if passed else "Fail")

test_sort()