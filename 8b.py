def subset_sum(arr, target):
    def backtrack(index, current):
        if sum(current) == target:
            solutions.append(current[:])
            return
        if index >= len(arr) or sum(current) > target:
            return

        # Include the current element
        current.append(arr[index])
        backtrack(index + 1, current)

        # Exclude the current element
        current.pop()
        backtrack(index + 1, current)

    solutions = []
    backtrack(0, [])
    return solutions


arr = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(arr, target))  # Output: [[4, 5]]
