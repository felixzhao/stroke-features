if __name__ == '__main__':
  fin = open('wubi_code_dict_6563.txt','r')
  line = fin.readline()
  terms = line.split(';')
  words = [w.split() for w in terms]
  dct = dict((w[0],w[1]) for w in wordlist[:-1])
