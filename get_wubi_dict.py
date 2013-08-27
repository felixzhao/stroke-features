
if __name__ == '__main__':
  fin = open('wubi_code.txt','r')
  fout = open('wubi_code_dict.txt','w')
  
  inlines = fin.readlines()
  for line in inlines:
    s = 0
    if len(line)%2 != 0: s = 1
    words = line.split()[1:]
    c = 0
    for w in words:
      if w != '\xe3\x80\x80':
        fout.write(str(w))
        c += 1
        if c%2 == 0:
          fout.write(';')
        else:
          fout.write(' ')
  
  fin.close()
  fout.close()