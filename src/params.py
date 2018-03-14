import random

def update_params(cur_tag, tag, sentence, feature, params, opt):
    flag = False
    ttags = (u"O", u"B-PER", u"I-PER", u"B-LOC", u"I-LOC", u"B-ORG", u"I-ORG")

    triple = ((u'O', u'B-LOC', u'B-LOC'), (u'B-PER', u'I-LOC', u'B-LOC'), (u'I-ORG', u'B-ORG', u'O'), (u'O', u'O', u'B-ORG'), (u'O', u'B-LOC', u'I-ORG'), (u'O', u'I-ORG', u'B-ORG'), (u'I-LOC', u'I-LOC', u'B-LOC'), (u'B-ORG', u'B-ORG', u'O'), (u'O', u'I-PER', u'I-PER'), (u'B-PER', u'I-ORG', u'B-ORG'), (u'I-ORG', u'B-ORG', u'I-PER'), (u'I-PER', u'B-PER', u'O'), (u'B-PER', u'O', u'O'), (u'I-PER', u'B-PER', u'I-ORG'), (u'O', u'O', u'I-LOC'), (u'I-LOC', u'I-LOC', u'I-LOC'), (u'O', u'B-PER', u'I-LOC'), (u'B-PER', u'I-ORG', u'I-ORG'), (u'O', u'B-LOC', u'I-LOC'), (u'O', u'B-PER', u'O'), (u'I-PER', u'I-PER', u'B-PER'), (u'O', u'I-LOC', u'I-LOC'), (u'B-LOC', u'I-LOC', u'B-LOC'), (u'B-ORG', u'I-LOC', u'B-LOC'), (u'I-LOC', u'B-LOC', u'I-LOC'), (u'B-ORG', u'I-PER', u'I-PER'), (u'O', u'B-LOC', u'O'), (u'B-ORG', u'I-ORG', u'B-ORG'), (u'B-LOC', u'O', u'B-LOC'), (u'O', u'B-ORG', u'O'), (u'O', u'I-ORG', u'I-ORG'), (u'B-LOC', u'O', u'I-ORG'), (u'O', u'O', u'B-PER'), (u'B-LOC', u'B-LOC', u'B-LOC'), (u'I-PER', u'B-PER', u'I-LOC'), (u'B-ORG', u'I-ORG', u'I-ORG'), (u'I-PER', u'I-PER', u'I-PER'), (u'B-LOC', u'I-ORG', u'I-ORG'), (u'I-LOC', u'B-LOC', u'I-PER'), (u'O', u'I-PER', u'B-PER'), (u'I-ORG', u'I-ORG', u'B-ORG'), (u'B-LOC', u'O', u'I-LOC'), (u'B-ORG', u'O', u'B-LOC'), (u'B-ORG', u'O', u'I-ORG'), (u'B-ORG', u'O', u'B-ORG'), (u'I-ORG', u'I-ORG', u'I-ORG'), (u'B-ORG', u'B-ORG', u'B-ORG'), (u'B-ORG', u'B-LOC', u'O'), (u'B-PER', u'B-PER', u'O'), (u'I-LOC', u'B-LOC', u'B-LOC'), (u'B-ORG', u'I-LOC', u'I-LOC'), (u'O', u'O', u'I-PER'), (u'B-LOC', u'I-LOC', u'I-LOC'), (u'O', u'I-LOC', u'B-LOC'), (u'B-ORG', u'O', u'I-LOC'), (u'O', u'O', u'O'), (u'B-PER', u'I-PER', u'B-PER'), (u'I-LOC', u'B-LOC', u'O'), (u'O', u'O', u'B-LOC'), (u'O', u'B-PER', u'B-PER'), (u'O', u'O', u'I-ORG'), (u'O', u'B-ORG', u'I-LOC'), (u'I-LOC', u'B-LOC', u'I-ORG'), (u'B-LOC', u'O', u'I-PER'), (u'B-PER', u'I-LOC', u'I-LOC'), (u'B-PER', u'O', u'I-LOC'), (u'O', u'B-ORG', u'B-LOC'), (u'B-PER', u'I-PER', u'I-PER'), (u'B-PER', u'O', u'B-PER'), (u'B-ORG', u'O', u'I-PER'), (u'B-LOC', u'I-PER', u'I-PER'), (u'B-LOC', u'B-LOC', u'O'), (u'O', u'B-PER', u'I-ORG'), (u'B-ORG', u'O', u'O'), (u'B-LOC', u'O', u'O'), (u'B-LOC', u'B-LOC', u'I-LOC'), (u'O', u'B-ORG', u'B-ORG'), (u'B-LOC', u'I-ORG', u'B-ORG'), (u'I-PER', u'B-PER', u'I-PER'), (u'B-PER', u'O', u'I-PER'), (u'I-ORG', u'B-ORG', u'I-ORG'), (u'I-ORG', u'B-ORG', u'B-LOC'), (u'I-ORG', u'B-ORG', u'I-LOC'), (u'B-ORG', u'I-PER', u'B-PER'), (u'B-PER', u'O', u'I-ORG'), (u'B-PER', u'O', u'B-LOC'))
    num = 0
    for i in range(len(cur_tag)):
        if(cur_tag[i] != tag[i]):
            flag = True
            num += 1
            #break;
    print "Dif: ",
    print num
    if(flag):
        for j in range(2, len(sentence)):
            v = ttags.index(tag[j])
            u = ttags.index(cur_tag[j])
            w = opt["charac"][sentence[j]]
            cor_sum = feature[j][(tag[j], tag[j - 1], tag[j - 2])][w + v * 4361]
            if((cur_tag[j], cur_tag[j-1], cur_tag[j - 2]) in triple):
                wrong_sum = feature[j][(cur_tag[j], cur_tag[j - 1], cur_tag[j - 2])][w + u * 4361]
            else:
                wrong_sum = 1

            params[w + v * 4361] += cor_sum

            params[w + u * 4361] -= wrong_sum
        for i in range(4361 * 7, len(params)):
            update = 0
            for j in range(2, len(tag)):
                

                ### To be written
                cor_sum = feature[j][(tag[j], tag[j - 1], tag[j - 2])][i]
                if((cur_tag[j], cur_tag[j-1], cur_tag[j - 2]) in triple):
                    wrong_sum = feature[j][(cur_tag[j], cur_tag[j - 1], cur_tag[j - 2])][i]
                else:
                    wrong_sum = 1             #print cor_sum,
                #print wrong_sum,
                update += cor_sum - wrong_sum
                
            #print update
            params[i] = params[i] + update;

def update_params_2(cur_tag, tag, sentence, feature, params, opt):
    flag = False
    ttags = (u"O", u"B-PER", u"I-PER", u"B-LOC", u"I-LOC", u"B-ORG", u"I-ORG")
    bi = ((u'B-PER', u'I-PER'), (u'B-PER', u'B-PER'), (u'B-LOC', u'I-LOC'), (u'B-LOC', u'I-ORG'), (u'B-ORG', u'O'), (u'O', u'B-PER'), (u'B-ORG', u'I-LOC'), (u'O', u'B-ORG'), (u'I-ORG', u'I-ORG'), (u'B-ORG', u'B-ORG'), (u'I-ORG', u'B-ORG'), (u'B-PER', u'I-ORG'), (u'B-PER', u'I-LOC'), (u'B-ORG', u'I-PER'), (u'I-PER', u'B-PER'), (u'O', u'O'), (u'O', u'I-ORG'), (u'B-LOC', u'I-PER'), (u'B-LOC', u'B-LOC'), (u'B-ORG', u'B-LOC'), (u'I-LOC', u'B-LOC'), (u'O', u'I-PER'), (u'O', u'I-LOC'), (u'B-PER', u'O'), (u'B-LOC', u'O'), (u'O', u'B-LOC'), (u'I-LOC', u'I-LOC'), (u'I-PER', u'I-PER'), (u'B-ORG', u'I-ORG'))
    num = 0
    sentence.extend([u"", u""])
    for i in range(len(cur_tag)):
        if(cur_tag[i] != tag[i]):
            flag = True
            num += 1
            #break;
    if(random.random() > 0.8):
        print "Dif: ",
        print num
    if(flag):
        for j in range(2, len(sentence) - 2):
            v = ttags.index(tag[j])
            u = ttags.index(cur_tag[j])

            
            for p in range(j - 2, j + 3):
                if(sentence[p] in opt["charac"]):
                    w = opt["charac"][sentence[p]]
                
                    params[w + v * 4361 + (p - j + 2) * 4361 * 7] += 1

                    params[w + u * 4361 + (p - j + 2) * 4361 * 7] -= 1
                    '''
                    cor_sum = feature[j][(tag[j], tag[j - 1])][w + v * 4361]
                    if((cur_tag[j], cur_tag[j-1]) in bi):
                        wrong_sum = feature[j][(cur_tag[j], cur_tag[j - 1])][w + u * 4361]
                    else:
                    wrong_sum = 1
                    '''
            for p in range(j - 2, j + 2):
                if((sentence[p], sentence[p + 1]) in opt["biword"]):
                    w = opt["biword"][(sentence[p], sentence[p+1])]
                    params[w + v * 89148 + (p - j + 2) * 89148 * 7 + 4361 * 7 * 5] += 1

                    params[w + u * 89148 + (p - j + 2) * 89148 * 7 + 4361 * 7 * 5] -= 1
                    
        for i in range(4361 * 7 * 5 + 4 * 89148 * 7, len(params)):
            update = 0
            for j in range(2, len(tag)):
                

                ### To be written
                cor_sum = feature[j][(tag[j], tag[j - 1])][i - 4361 * 7 * 5 - 4 * 89148 * 7]
                if((cur_tag[j], cur_tag[j-1]) in bi):
                    wrong_sum = feature[j][(cur_tag[j], cur_tag[j - 1])][i - 4361 * 7 * 5 - 4 * 89148 * 7]
                else:
                    wrong_sum = 1             #print cor_sum,
                #print wrong_sum,
                update += cor_sum - wrong_sum
                
            #print update
            params[i] = params[i] + update;
    sentence.pop()
    sentence.pop()
        
     
