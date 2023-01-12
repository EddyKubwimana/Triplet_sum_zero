def find_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l = i+1
        r = len(arr)-1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s == 0:
                triplets.append((arr[i], arr[l], arr[r]))
                l += 1
                r -= 1
                while l < r and arr[l] == arr[l-1]:
                    l += 1
                while l < r and arr[r] == arr[r+1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return triplets


numbers = [1,2, -1, -1, 9, -9, 0,2]

print(find_triplets(numbers))
