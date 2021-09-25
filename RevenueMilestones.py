def getMilestoneDays(revenues, milestones):
  # Write your code here
  
  output = []
  cummulative = []
  rev = 0
  for r in revenues:
    rev += r
    cummulative.append(rev)
 
  for m in milestones:
    mid = int(len(cummulative)/2)
    has_val = False
    
    while has_val == False and mid < len(cummulative) - 1 and mid > 0:
      if (cummulative[mid] >=  m and cummulative[mid - 1] < m) :
        output.append(mid + 1)
        has_val = True
      if (cummulative[mid] <  m and cummulative[mid + 1] >= m):
        output.append(mid + 2)
        has_val = True
      if m > cummulative[mid]:
        mid = int((mid + len(cummulative) - 1)/2)
      if m < cummulative[mid]:
        mid = int(mid/2)
        
    if has_val == False:
      output.append(-1)
    
  return output
###O(Mlog(N))
