
def cal_feature(i, sentence, tag, opt):
    
    array_feature = []   
    tags = ("O", "B-PER", "I-PER", "B-LOC", "I-LOC", "B-ORG", "I-ORG")
    #for i in range(len(sentence)):

    #array_feature = [0] * (4361 * 7)

    sentence.append(u"")
    sentence.append(u"")

    '''
    for it in range(4361 * 7):
        array_feature.append(0)
    '''
    v = tags.index(tag[0])
    #print opt["charac"][sentence[i]]
    #array_feature[opt["charac"][sentence[i]] + v * 4361] = 1

    array_feature.append(check(sentence[i], tag[0], opt["B-PER"], "B-PER"))
    array_feature.append(check(sentence[i - 1], tag[0], opt["B-PER"], "I-PER"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["B-PER"], "I-PER"))

    array_feature.append(check(sentence[i - 1], tag[0], opt["I-LOC"], "I-LOC"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["I-LOC"], "I-LOC"))    
    array_feature.append(check(sentence[i], tag[0], opt["B-LOC"], "B-LOC"))
    array_feature.append(check(sentence[i + 1], tag[0], opt["I-LOC"], "I-LOC"))
    array_feature.append(check(sentence[i + 2], tag[0], opt["I-LOC"], "I-LOC"))
    array_feature.append(check(sentence[i + 1], tag[0], opt["I-LOC"], "B-LOC"))
    array_feature.append(check(sentence[i + 2], tag[0], opt["I-LOC"], "B-LOC"))
    
    array_feature.append(check(sentence[i], tag[0], opt["B-ORG"], "B-ORG"))
    array_feature.append(check(sentence[i - 1], tag[0], opt["I-ORG"], "I-ORG"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["I-ORG"], "I-ORG"))
    array_feature.append(check(sentence[i - 1], tag[0], opt["B-ORG"], "I-ORG"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["B-ORG"], "I-ORG"))
    array_feature.append(check(sentence[i + 1], tag[0], opt["I-ORG"], "B-ORG"))
    array_feature.append(check(sentence[i + 2], tag[0], opt["I-ORG"], "B-ORG"))

    array_feature.append(check(sentence[i], tag[0], opt["B-PER"], "O"))
    array_feature.append(check(sentence[i - 1], tag[0], opt["B-PER"], "O"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["B-PER"], "O"))

    array_feature.append(check(sentence[i - 1], tag[0], opt["I-LOC"], "O"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["I-LOC"], "O"))    
    array_feature.append(check(sentence[i], tag[0], opt["B-LOC"], "O"))
    array_feature.append(check(sentence[i + 1], tag[0], opt["I-LOC"], "O"))
    array_feature.append(check(sentence[i + 2], tag[0], opt["I-LOC"], "O"))
    array_feature.append(check(sentence[i + 1], tag[0], opt["I-LOC"], "O"))
    array_feature.append(check(sentence[i + 2], tag[0], opt["I-LOC"], "O"))
    
    array_feature.append(check(sentence[i], tag[0], opt["B-ORG"], "O"))
    array_feature.append(check(sentence[i - 1], tag[0], opt["I-ORG"], "O"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["I-ORG"], "O"))
    array_feature.append(check(sentence[i - 1], tag[0], opt["B-ORG"], "O"))
    array_feature.append(check(sentence[i - 2], tag[0], opt["B-ORG"], "O"))
    array_feature.append(check(sentence[i + 1], tag[0], opt["I-ORG"], "O"))
    array_feature.append(check(sentence[i + 2], tag[0], opt["I-ORG"], "O"))



       #  array_feature.append(   check_org(sentence, i, tag)
       #  array_feature.append(   check_loc(sentence, i, tag, features)
       #  array_feature.append(   check_next_word(sentence[i + 1], tag, features)
       #  array_feature.append(   check_two_ahead(sentence[i + 2], tag, features)
    sentence.pop()
    sentence.pop()

    return array_feature



def check(word, tag, opt, cmp_tag):
    if(search(word, opt) and tag == cmp_tag):
        return 1
    else:
        return 0

def check_last_name_around(word, tag, opt):
    if(search(word, opt) and tag == "I-PER"):
        return 1
    else:
        return 0

def search(word, diction):
    if(word in diction):
        if(diction[word] > 10):
        #print word
            return True
        else:
            return False
    else:
        return False
'''    
def search(word, filename):
    #return False
    # Slow!!!!!!!!!!
    f = open(filename)
    flag = False
    try:
        str = f.read()
        print "Word: "
        print word
        print "Result: "
        print str.find(word)
    ### Potential bugs here
        if(str.find(word)):
            flag = True
        else:
            flag = False
    finally:
        f.close()
        return flag
'''
