###

# this code is use to 
# top n words
# which are top match score with input word
# the match score is calculate by stroke feature (Wubi)
# score = intersect_length( source_word, target_word ) / code_length
# source word : Wubi code for source word which in wubi code dict
# target word : stroke code (Wubi) for target word which is the word need to find similar words
# code length : Wubi code length is 4

###

import sys

# if return 0 means no match
def get_match_score(stroke_code_tuple_list, target_stroke, size):
  result = []
  code_length = 4
  for tuple in stroke_code_tuple_list:
    print '========================='
    print 'for word' + tuple[0] + tuple[1]
    match_score = len(set(tuple[1]) & set(target_stroke)) / float(code_length)
    print match_score
    if(match_score > 0):
      result.append((tuple[0],match_score))
  result.sort(key=lambda tup: tup[1])
  return result[:size]

if __name__ == '__main__':
  stroke_code_file = 'C:\\Users\\zhaoqua\\Documents\\GitHub\\stroke-features\\wubi_code_dict_6563.txt'
  fout = open('e:\\match_out.txt','w')
  target_stroke = 'ulmk'
  
  terms = open(stroke_code_file,'r').readline().split(';')
  words = [w.split() for w in terms]
  stroke_code_tuple_list = [(w[0],w[1]) for w in words[:-1]]
  
  size = 50
  match_score_list = get_match_score(stroke_code_tuple_list, target_stroke, size)
  print('target: ' + target_stroke)
  print(len(match_score_list))
  for w in match_score_list:
    #print(w[0])
    #print(w[1])
    # out to file
    fout.write(w[0] + ',' + str(w[1])+ '\n')
  fout.close()