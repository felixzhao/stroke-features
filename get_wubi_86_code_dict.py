
if __name__ == '__main__':
  fin = open('e:\\wubi_86_code.txt','r')
  fout = open('wubi_86_code_dict.txt','w')
  
  inlines = fin.readlines()
  for line in inlines:
    words = line.split()
    if len(words) < 2: continue
    fout.write(words[0] + ' ' + words[1] + ';')
  
  fin.close()
  fout.close()