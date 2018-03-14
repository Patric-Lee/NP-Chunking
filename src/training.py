from read_line import *
from Viterbi import *
from params import *
import codecs
import random
def training(pass_num, data_set, feature_num):
    # Initiate parameters to be all zeros
    data = data_set[0]
    params = []
    opt = data_set[1]
    #opt.append(read_dict("LastNames.txt"))
    for i in range(feature_num):
        params.append(0)
  
    for i in range(pass_num):
        print len(data)
        random.shuffle(data)
        j = 0
        for d in data:
            # Process the original data
            # Incorporate two start symbol for convenience
            sentence = [u"", u""]
            sentence.extend(d[0])
            #print sentence
            tag = [u"O", u"O"]
            tag.extend(d[1])

            #print sentence
            #print tag
            tmp = viterbi_bi(sentence, params, opt)
            cur_tag = tmp[0]
            feature = tmp[1]
            #print cur_tag
            #print tag
            update_params_2(cur_tag, tag, sentence, feature, params, opt)
            if(j % 100 == 0):
                print j,
                print " ",
                print i
                pp = open("param", "w")
                for par in params:
                    pp.write(str(par) + " ")
                #print params
            j = j+1
            #print j


            ### To be deleted!!!!!!!!
            #if(j == 500):
             #   break;
            



    return params

def assess(params, data):
    predicted = codecs.open("predicted", "w", encoding="utf-8")
    golden = codecs.open("golden", "w", encoding="utf-8")
    print len(data[2])
    it = 0
    for d in data[2]:
        #print d[0]
        #print d[1]
        sentence = [u"", u""]
        sentence.extend(d[0])
        tmp = viterbi_bi(sentence, params, data[1])
        cur_tag = tmp[0]
        #print cur_tag
        tag = d[1]
        str_cur = u""
        for i in range(2, len(cur_tag)):
            str_cur += sentence[i] + u" " + cur_tag[i] + u"\n"
        str_cur += u"\n"
        predicted.write(str_cur)
        str_tag = u""
        for i in range(len(tag)):
            str_tag += d[0][i] + u" " + tag[i] + u"\n"
        str_tag += u"\n"
        golden.write(str_tag)
        if(it % 100 == 0):
            print it
        it = it + 1
    predicted.close()
    golden.close()
    
c = read_training()
params = training(10, c, 34 + 4361 * 7 * 5 + 4 * 7 * 89148)
#params = [98, 180, -1236, -1152, 294, -5, 481, -1340, 448, -451, -508, 6, -773, 192, -1397, 294, -992]
assess(params, c)
