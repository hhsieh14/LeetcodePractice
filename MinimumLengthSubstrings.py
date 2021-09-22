"""
Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
"""



def min_length_substring(s, t):
  # Write your code here
  table_count = {}
  for c in t:
    if c in table_count:
      table_count[c] += 1
    else:
      table_count[c] = 1
  table_index = {}
  
  for i, c in enumerate(s):
    if c in table_index:
      table_index[c].append(i)
    else:
      table_index[c] = [i, ]
      
  max_list = []
  min_list = []
  
  for key, value in table_count.items():
    if key not in table_index or len(table_index[key]) < value:
      return - 1
    elif key in table_index and len(table_index[key]) >= value:
      max_list.append(table_index[key][-1 * value])
      min_list.append(table_index[key][value - 1])
      
  len_max = max(max_list) - min(max_list) + 1
  
  len_min = max(min_list) - min(min_list) + 1
 
  
  return len_max if len_max <= len_min else len_min
