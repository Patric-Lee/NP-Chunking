from Viterbi import *
from read_line import read_training

import codecs
def read_param():
    par = open("param")
    t = []
    if(True):
        l = par.readline()
        p = l.split(' ')
        print p[-1]
        print len(p)
        i = 0
        for pa in p:
            if(pa != ''):
                t.append(int(pa))
            
        print "a"
        print len(t)
    
    return t

def read_testing():
    test_data = open('ner_tst_wol')
    data = []
    sentence = []
    i = 0
    try:
        while(1):
            lines = test_data.readlines(100000)
            if(not lines):
                break;
            for line in lines:
                if(line == '\n'):
                    data.append(sentence)
                    '''
                    print sentence[-1]
                    for s in sentence:
                        print s,
                    print '\n'
                    '''
                    sentence = []
                else:
                    sentence.append(unicode(line, "utf-8")[0])
                    #print sentence[-1]
                i += 1
                if(i % 1000 ==0):
                    print i
    finally:
        
        print len(data)
        return data

def assess(params, data, opt):
    predicted = codecs.open("predicted", "w", encoding="utf-8")
    #golden = codecs.open("golden", "w", encoding="utf-8")
    print len(data)
    it = 0
    for d in data:
        #print d[0]
        #print d[1]
        sentence = [u"", u""]
        sentence.extend(d)
        tmp = viterbi_bi(sentence, params, opt)
        cur_tag = tmp[0]
        #print cur_tag
        #tag = d[1]
        str_cur = u""
        for i in range(2, len(cur_tag)):
            str_cur += sentence[i] + u" " + cur_tag[i] + u"\n"
        str_cur += u"\n"
        predicted.write(str_cur)
        '''
        str_tag = u""
        for i in range(len(tag)):
            str_tag += d[0][i] + u" " + tag[i] + u"\n"
        str_tag += u"\n"
        golden.write(str_tag)
        '''
        if(it % 100 == 0):
            print it
        it = it + 1
    predicted.close()
    #golden.close()
    
c = read_training()
params = read_param()
test = read_testing()
assess(params, test, c[1])
#params = [98, 180, -1236, -1152, 294, -5, 481, -1340, 448, -451, -508, 6, -773, 192, -1397, 294, -992]
#assess(params, c)






