def minimumSwaps(arr):
  swaps = 0
  n = len(arr)
  for i in range(0, n):
    while arr[i] != i + 1:
      t = arr[arr[i] - 1]
      arr[arr[i] - 1] = arr[i]
      arr[i] = t
      swaps += 1

  return swaps

a = [1,3,5,2,4,6,7]
res = minimumSwaps(a)
print(res)
