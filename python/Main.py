from python.RemoveDuplicatesfromSortedArray import Solution


def main():
    print("###  Testing Solution  ###")

    s = Solution()

    print("\n  >> Testing #1 Set")
    s.removeElement([1, 1, 2])

    print("\n  >> Testing #2 Set")
    s.removeElement([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

    print("\n###  All tests passed!  ###")


if __name__ == '__main__':
    main()
