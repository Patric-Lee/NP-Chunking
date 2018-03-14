import re, collections



def read_training():
    training_data = open('ner_trn')
    try:
        #trigram = set()
        bigram = set()
        biword = {}
        data = {}
        data["train"] = []
        data["test"] = []
        sentence = []
        tags = []
        i = 0
        bbword = {}
        ss = "train"
        opt = {}
        tags_ = ("B-PER", "I-PER", "B-LOC", "I-LOC", "B-ORG", "I-ORG")
        words = {}
        charac = {}
        '''
        words["PER"] = {}
        words["LOC"] = {}
        words["ORG"] = {}
        '''
        for t in tags_:
            opt[t] = {}
        opt["charac"] = charac
        opt["biword"] = bbword

        stat_word = u""
        while(1):

            lines = training_data.readlines(100000)
            if(not lines):
                break;
            #if(i > 45):
             #   ss = "test"
            for line in lines:
                if(line == "\n"):
                    data[ss].append((sentence, tags))
                    sentence = []
                    tags = []
                else:
                    #print unicode(line, "utf-8")[0]
                    #print unicode(line, "utf-8")[2:]
                    sentence.append(unicode(line, "utf-8")[0])
                    tags.append(unicode(line, "utf-8")[2:-1])

                    if(tags[-1] in tags_):
                        stat_word += sentence[-1]
                        if(sentence[-1] in opt[tags[-1]]):
                            opt[tags[-1]][sentence[-1]] += 1

                        else:
                            opt[tags[-1]][sentence[-1]] = 1
                    else:
                        if(stat_word != u""):
                            if(stat_word in words):
                                words[stat_word] += 1
                            else:
                                words[stat_word] = 1
                            stat_word = u""
                    if(not sentence[-1] in charac):
                        
                        charac[sentence[-1]] = len(charac)


                    if(len(tags) > 1):
                        bigram.add((tags[-1], tags[-2]))
                    if(len(sentence) > 1 and not (sentence[-2], sentence[-1]) in biword):
                        biword[(sentence[-2], sentence[-1])] = len(biword)
                    elif(len(sentence) > 1 and (sentence[-2], sentence[-1]) in biword and not (sentence[-2],sentence[-1]) in bbword):
                        bbword[(sentence[-2], sentence[-1])] = len(bbword)
                        #print len(bbword)
                    



                    
                #else if(line and unicode(line, "utf-8")[0] == '\n'
            i = i + 1
            print i
            '''
            d = data[-1]
            
            for u in d[0]:
                print u,
            for u in d[1]:
                print u,
            print "\n"
            '''
        '''
        for tt in tags_:
            print tt
            diction = opt[tt]
            new_dict = sorted(diction.items(), key=lambda loc:loc[1], reverse=True)
            for nn in new_dict:
                print nn[0],
                print nn[1]
        '''
        '''
        new_dict = sorted(words.items(), key=lambda loc:loc[1], reverse=True)
        for tt in new_dict:
            print tt[0],
            print tt[1]
        '''


        ''' 
             
        location = sorted(loc.items(), key=lambda loc:loc[1], reverse=True)
        for l in location:
            print l[0],
            print l[1]
        '''
    
    finally:
        print bigram
        print len(bigram)
        print len(bbword)
        print len(biword)
        training_data.close()
    return (data["train"], opt, data["test"])





def read_dict(filename):
    data = set()
    f = open(filename)
    try:
        str = f.read()
        #print str
        #print "b"
        
        #print t
        data = set(unicode(str, "utf-8"))
        #data.remove(u"")
        #data.remove(u"\n")
        #for u in data:
         #   print u
    finally:
        f.close()
        return data


    
read_training()
