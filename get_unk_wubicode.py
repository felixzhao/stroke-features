infile_wordmap = open('E:\w1\unk_wordmap.txt','r')
infile_wubi = open('E:\w1\wubi_code_6563.txt','r')
outfile = open('E:\w1\out.txt','w')

dict_wordmap = {}
dict_wubi = {}

### generate word map dict
lines_wordmap = infile_wordmap.readlines()
for line in lines_wordmap:
  wordmap = line.split()
  dict_wordmap[wordmap[0]] = wordmap[1]
  
### generate wubi dict
lines_wubi = infile_wubi.readlines()
for line in lines_wubi:
  wubi = line.split()
  if len(wubi) < 2:
    print wubi
  else:
    dict_wubi[wubi[0]] = wubi[1]
  
### get unk wubi mapping
for k in dict_wordmap.keys():
  if dict_wordmap[k] in dict_wubi:
    print '{0} {1}'.format(k, dict_wubi[dict_wordmap[k]])
    print >> outfile, '{0} {1}'.format(k, dict_wubi[dict_wordmap[k]])
'''  else:
    print '*** {0} {1}'.format(k, dict_wordmap[k])
    print >> outfile, '*** {0} {1}'.format(k, dict_wordmap[k])
'''
outfile.close()