def subsets(i, arr, n, s, currset):
    if i == n:
        s.add(tuple(currset))  # Convert list to tuple before adding to the set
        return
    subsets(i + 1, arr, n, s, currset)
    currset.append(arr[i])
    subsets(i + 1, arr, n, s, currset)
    currset.pop()

def print_subsets(s):
    for x in sorted(s):
        print("(", end="")
        print(" ".join(map(str, x)), end="")
        print(")", end="")
    print()

def main():
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter number of elements: "))
        arr = list(map(int, input("Enter the elements: ").split()))

        arr.sort()
        s = set()
        currset = []
        subsets(0, arr, n, s, currset)
        print_subsets(s)

if __name__ == "__main__":
    main()
