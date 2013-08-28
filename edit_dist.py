def editdist(a, b):
  """
  Recursively calculate the Levenshtein edit distance between two strings, a and b.
  Returns the edit distance.
  """
  if("" == a): 
    return len(b) # returns if a is an empty string
  if("" == b): 
    return len(a) # returns if b is an empty string
  return min(
                  editdist(a[:-1], b[:-1]) + (a[-1] != b[-1]), 
                  editdist(a[:-1], b)+1, 
                  editdist(a, b[:-1])+1
                 ) 
if __name__ == '__main__':
  source = 'pantera'
  target = 'aorta'
  expected = 5
  actual = editdist(source, target)
  print('expected: ' + str(expected))
  print('actual: ' + str(actual))
  print(expected == actual)