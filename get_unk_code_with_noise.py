import sys

noise_size = int(sys.argv[1])

#if noise_size < 1 or noise_size > 4:
#    noise_size = 0
    
noise = 'z'*noise_size

wordmap = open('word-map.txt','r')
strokeCode = open('wubi_code_dict_6563.txt','r')

stroke_code_file = 'wubi_code_dict_6563.txt'
terms = open(stroke_code_file,'r').readline().split(';')
wordmap = open('word-map.txt','r').readlines()
fout = open('unk_code_'+ str(noise_size) + '.txt','w')

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
        code = noise + stroke_dict[k][noise_size:]
        
        print k,code
        print >> fout,k,code

print noise_size
