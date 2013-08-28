import sys
import stroke_intersection

def find_match(stroke_code_tuple_list, target_stroke):
  result = []
  max = 0
  for tuple in stroke_code_tuple_list:
    intersection = stroke_intersection.stroke_intersection(tuple[1], target_stroke)
    if intersection > max:
      max = intersection
      result = []
      result.append(tuple)
    elif intersection == max:
      result.append(tuple)
  return result

if __name__ == '__main__':
  stroke_code_file = 'e:\\wubi_code_dict_6563.txt'
  fout = open('e:\\match_out.txt','w')
  target_stroke = 'bk'
  
  terms = open(stroke_code_file,'r').readline().split(';')
  words = [w.split() for w in terms]
  stroke_code_tuple_list = [(w[0],w[1]) for w in words[:-1]]
  
  match_word_list = find_match(stroke_code_tuple_list, target_stroke)
  print('target: ' + target_stroke)
  print(len(match_word_list))
  for w in match_word_list:
    print(w[0])
    print(w[1])
    # out to file
    fout.write(w[0] + ',' + w[1]+ ';')
  fout.close()
  