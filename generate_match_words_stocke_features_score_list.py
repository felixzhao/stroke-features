
def get_match_words(word_map_path):
  word_map_dict = {}

  word_map = open(word_map_path,'rb')
  for line in word_map.readlines():
    term = line.split()
    if len(term) < 2:
      continue
    else:
      word_map_dict[term[1]] = term[0]
      
  return word_map_dict

def get_stocke_feature_dict(stroke_code_file):
  result = {}
  terms = open(stroke_code_file,'r').readline().split(';')
  words = [w.split() for w in terms]
  result = {(w[0],w[1]) for w in words[:-1]}
  return result 
  
if __name__ == '__main__':
  word_map_path = 'word-map-33percent.txt'
  stroke_code_file = 'wubi_code_dict_6563.txt'
  out_path = 'unk_map.txt'
  
  ## stocke feature code
  stocke_feature_dict = get_stocke_feature_dict(stroke_code_file)
  
  ## word map info
  word_map = get_match_words(word_map_path)
  
  out_file = open(out_path,'w')
  for key in word_map.keys():
    unk_map_item = '{0} {1}'.format(key, word_map[key])
    if key in stocke_feature_dict:
      unk_map_item += ' {0}'.format(stocke_feature_dict[key])
    else:
      unk_map_item += ' no_code'
    print >> out_file, unk_map_item
    print unk_map_item
  