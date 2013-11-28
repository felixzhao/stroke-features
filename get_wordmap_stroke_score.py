
def get_stroke_score_dict():
  result = {}
  temp = []
  
  words = open('wubi_words.txt','r').readlines()
  codes = open('wubi_stroke_code.txt','r').readlines()
  
  if len(words) != len(codes):
    print 'length not match.'
    print len(words)
    print len(codes)
    
  for i in xrange(len(words)):
    temp.append((words[i],codes[i]))
  
  for item in temp:
    result[item[0]] = item[1]
  
  return result

def get_score():
  fin = open('wubi_code_dict_6563_multiline.txt','r')
  
  result = {}
  
  lines = fin.readlines()[3]
  
  for line in lines:
    pair = line.split(',')
    print len(pair)
    for item in pair:
      print item
    print '------'
  
  return result

if __name__ == '__main__':  
  stroke_dict = get_stroke_score_dict()
  for k in stroke_dict:
    print str(k)
    print stroke_dict[k]
    print ' --- --- '