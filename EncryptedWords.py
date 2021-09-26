
def findEncryptedWord(s):
  # Write your code here
  mid = int((len(s)- 1)/2)
  sub1 = s[:mid]
  sub2 = s[mid + 1: ]
  enc = ""
  enc += s[mid]
  if len(sub1) >= 3:
    enc += findEncryptedWord(sub1)
  else:
    enc += sub1
  if len(sub2)>= 3:
    enc += findEncryptedWord(sub2)
  else:
    enc += sub2
    
  return enc
