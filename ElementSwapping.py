def findMinArray(arr, k):
  # Write your code here
  
  
  for i in range(len(arr)):
    min_val = (arr[i], i)
    for j in range(i+1, i+k):
      if min_val[0] > arr[j]:
        min_val = (arr[j], j)
    if min_val[0] < arr[i]:
      break
 
  for i in range(min_val[1], min_val[1]-k, -1):
    temp = arr[i]
    arr[i] = arr[i -1]
    arr[i-1] = temp
  return arr
