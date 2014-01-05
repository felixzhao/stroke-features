import sys

word_map_file = sys.argv[1]
noise_size = int(sys.argv[2])
word_map_type = sys.argv[3]
    
noise = 'z'*noise_size

stroke_code_file = 'wubi_code_dict_6563.txt'
terms = open(stroke_code_file,'r').readline().split(';')
wordmap = open(word_map_file,'r').readlines() #'word-map.txt','r').readlines()
fout = open('unk_code_ns'+ str(noise_size) + '_type' + word_map_type + '.txt','w')

stroke_dict = {}
unk_dict = {}

words = [w.split() for w in terms]
for w in words:
    if len(w) > 1:
        stroke_dict[w[0]] = w[1]
for line in wordmap:
    w = line.split(' ')
    if len(w) > 1:
        unk_dict[w[0]] = w[1]

for k in unk_dict.keys():
    if k in stroke_dict:
        ## add noise
        code = stroke_dict[k][:len(stroke_dict[k]) - noise_size] + noise
        
        print unk_dict[k][:-1], code
        print >> fout, unk_dict[k][:-1], code

print noise_size
