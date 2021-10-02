def findSignatureCounts(arr):
  # Write your code here
  #the number of signitures depends on how many people are in the passing loop
  #first find out the number of people who just pass his book to himself.
  #the other people's book will obtain len(arr) - the number of people who just pass his book to himself.
  
  n = len(arr)
  output = []
  count = 0
  for i in range(n):
    if arr[i] - 1 == i:
      count += 1
  sig = n - count
  for i in range(n):
    if arr[i] - 1 == i:
      output.append(1)
    else:
      output.append(sig)
  return output
