def stroke_intersection(source, target):
  return len(set(source) & set(target))

if __name__ == '__main__':
  source = 'abc'
  target = 'gca'
  expected = 2
  actual = stroke_intersection(source, target)
  print(expected == actual)