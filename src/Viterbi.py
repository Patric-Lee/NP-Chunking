from feature import *

def viterbi(sentence, params, opt):
    tags = (u"O", u"B-PER", u"I-PER", u"B-LOC", u"I-LOC", u"B-ORG", u"I-ORG")

    triple = ((u'O', u'B-LOC', u'B-LOC'), (u'B-PER', u'I-LOC', u'B-LOC'), (u'I-ORG', u'B-ORG', u'O'), (u'O', u'O', u'B-ORG'), (u'O', u'B-LOC', u'I-ORG'), (u'O', u'I-ORG', u'B-ORG'), (u'I-LOC', u'I-LOC', u'B-LOC'), (u'B-ORG', u'B-ORG', u'O'), (u'O', u'I-PER', u'I-PER'), (u'B-PER', u'I-ORG', u'B-ORG'), (u'I-ORG', u'B-ORG', u'I-PER'), (u'I-PER', u'B-PER', u'O'), (u'B-PER', u'O', u'O'), (u'I-PER', u'B-PER', u'I-ORG'), (u'O', u'O', u'I-LOC'), (u'I-LOC', u'I-LOC', u'I-LOC'), (u'O', u'B-PER', u'I-LOC'), (u'B-PER', u'I-ORG', u'I-ORG'), (u'O', u'B-LOC', u'I-LOC'), (u'O', u'B-PER', u'O'), (u'I-PER', u'I-PER', u'B-PER'), (u'O', u'I-LOC', u'I-LOC'), (u'B-LOC', u'I-LOC', u'B-LOC'), (u'B-ORG', u'I-LOC', u'B-LOC'), (u'I-LOC', u'B-LOC', u'I-LOC'), (u'B-ORG', u'I-PER', u'I-PER'), (u'O', u'B-LOC', u'O'), (u'B-ORG', u'I-ORG', u'B-ORG'), (u'B-LOC', u'O', u'B-LOC'), (u'O', u'B-ORG', u'O'), (u'O', u'I-ORG', u'I-ORG'), (u'B-LOC', u'O', u'I-ORG'), (u'O', u'O', u'B-PER'), (u'B-LOC', u'B-LOC', u'B-LOC'), (u'I-PER', u'B-PER', u'I-LOC'), (u'B-ORG', u'I-ORG', u'I-ORG'), (u'I-PER', u'I-PER', u'I-PER'), (u'B-LOC', u'I-ORG', u'I-ORG'), (u'I-LOC', u'B-LOC', u'I-PER'), (u'O', u'I-PER', u'B-PER'), (u'I-ORG', u'I-ORG', u'B-ORG'), (u'B-LOC', u'O', u'I-LOC'), (u'B-ORG', u'O', u'B-LOC'), (u'B-ORG', u'O', u'I-ORG'), (u'B-ORG', u'O', u'B-ORG'), (u'I-ORG', u'I-ORG', u'I-ORG'), (u'B-ORG', u'B-ORG', u'B-ORG'), (u'B-ORG', u'B-LOC', u'O'), (u'B-PER', u'B-PER', u'O'), (u'I-LOC', u'B-LOC', u'B-LOC'), (u'B-ORG', u'I-LOC', u'I-LOC'), (u'O', u'O', u'I-PER'), (u'B-LOC', u'I-LOC', u'I-LOC'), (u'O', u'I-LOC', u'B-LOC'), (u'B-ORG', u'O', u'I-LOC'), (u'O', u'O', u'O'), (u'B-PER', u'I-PER', u'B-PER'), (u'I-LOC', u'B-LOC', u'O'), (u'O', u'O', u'B-LOC'), (u'O', u'B-PER', u'B-PER'), (u'O', u'O', u'I-ORG'), (u'O', u'B-ORG', u'I-LOC'), (u'I-LOC', u'B-LOC', u'I-ORG'), (u'B-LOC', u'O', u'I-PER'), (u'B-PER', u'I-LOC', u'I-LOC'), (u'B-PER', u'O', u'I-LOC'), (u'O', u'B-ORG', u'B-LOC'), (u'B-PER', u'I-PER', u'I-PER'), (u'B-PER', u'O', u'B-PER'), (u'B-ORG', u'O', u'I-PER'), (u'B-LOC', u'I-PER', u'I-PER'), (u'B-LOC', u'B-LOC', u'O'), (u'O', u'B-PER', u'I-ORG'), (u'B-ORG', u'O', u'O'), (u'B-LOC', u'O', u'O'), (u'B-LOC', u'B-LOC', u'I-LOC'), (u'O', u'B-ORG', u'B-ORG'), (u'B-LOC', u'I-ORG', u'B-ORG'), (u'I-PER', u'B-PER', u'I-PER'), (u'B-PER', u'O', u'I-PER'), (u'I-ORG', u'B-ORG', u'I-ORG'), (u'I-ORG', u'B-ORG', u'B-LOC'), (u'I-ORG', u'B-ORG', u'I-LOC'), (u'B-ORG', u'I-PER', u'B-PER'), (u'B-PER', u'O', u'I-ORG'), (u'B-PER', u'O', u'B-LOC'))
    #triple = ((u'O', u'O', u'O') , (u'B-PER', u'O', u'O') , (u'B-LOC', u'O', u'O') , (u'B-ORG', u'O', u'O') , (u'O', u'B-PER', u'O') , (u'B-PER', u'B-PER', u'O') , (u'I-PER', u'B-PER', u'O') , (u'B-LOC', u'B-PER', u'O') , (u'B-ORG', u'B-PER', u'O') , (u'O', u'B-LOC', u'O') , (u'B-PER', u'B-LOC', u'O') , (u'B-LOC', u'B-LOC', u'O') , (u'I-LOC', u'B-LOC', u'O') , (u'B-ORG', u'B-LOC', u'O') , (u'O', u'B-ORG', u'O') , (u'B-PER', u'B-ORG', u'O') , (u'B-LOC', u'B-ORG', u'O') , (u'B-ORG', u'B-ORG', u'O') , (u'I-ORG', u'B-ORG', u'O') , (u'O', u'O', u'B-PER') , (u'B-PER', u'O', u'B-PER') , (u'B-LOC', u'O', u'B-PER') , (u'B-ORG', u'O', u'B-PER') , (u'O', u'B-PER', u'B-PER') , (u'B-PER', u'B-PER', u'B-PER') , (u'I-PER', u'B-PER', u'B-PER') , (u'B-LOC', u'B-PER', u'B-PER') , (u'B-ORG', u'B-PER', u'B-PER') , (u'O', u'I-PER', u'B-PER') , (u'B-PER', u'I-PER', u'B-PER') , (u'I-PER', u'I-PER', u'B-PER') , (u'B-LOC', u'I-PER', u'B-PER') , (u'B-ORG', u'I-PER', u'B-PER') , (u'O', u'B-LOC', u'B-PER') , (u'B-PER', u'B-LOC', u'B-PER') , (u'B-LOC', u'B-LOC', u'B-PER') , (u'I-LOC', u'B-LOC', u'B-PER') , (u'B-ORG', u'B-LOC', u'B-PER') , (u'O', u'B-ORG', u'B-PER') , (u'B-PER', u'B-ORG', u'B-PER') , (u'B-LOC', u'B-ORG', u'B-PER') , (u'B-ORG', u'B-ORG', u'B-PER') , (u'I-ORG', u'B-ORG', u'B-PER') , (u'O', u'O', u'I-PER') , (u'B-PER', u'O', u'I-PER') , (u'B-LOC', u'O', u'I-PER') , (u'B-ORG', u'O', u'I-PER') , (u'O', u'B-PER', u'I-PER') , (u'B-PER', u'B-PER', u'I-PER') , (u'I-PER', u'B-PER', u'I-PER') , (u'B-LOC', u'B-PER', u'I-PER') , (u'B-ORG', u'B-PER', u'I-PER') , (u'O', u'I-PER', u'I-PER') , (u'B-PER', u'I-PER', u'I-PER') , (u'I-PER', u'I-PER', u'I-PER') , (u'B-LOC', u'I-PER', u'I-PER') , (u'B-ORG', u'I-PER', u'I-PER') , (u'O', u'B-LOC', u'I-PER') , (u'B-PER', u'B-LOC', u'I-PER') , (u'B-LOC', u'B-LOC', u'I-PER') , (u'I-LOC', u'B-LOC', u'I-PER') , (u'B-ORG', u'B-LOC', u'I-PER') , (u'O', u'B-ORG', u'I-PER') , (u'B-PER', u'B-ORG', u'I-PER') , (u'B-LOC', u'B-ORG', u'I-PER') , (u'B-ORG', u'B-ORG', u'I-PER') , (u'I-ORG', u'B-ORG', u'I-PER') , (u'O', u'O', u'B-LOC') , (u'B-PER', u'O', u'B-LOC') , (u'B-LOC', u'O', u'B-LOC') , (u'B-ORG', u'O', u'B-LOC') , (u'O', u'B-PER', u'B-LOC') , (u'B-PER', u'B-PER', u'B-LOC') , (u'I-PER', u'B-PER', u'B-LOC') , (u'B-LOC', u'B-PER', u'B-LOC') , (u'B-ORG', u'B-PER', u'B-LOC') , (u'O', u'B-LOC', u'B-LOC') , (u'B-PER', u'B-LOC', u'B-LOC') , (u'B-LOC', u'B-LOC', u'B-LOC') , (u'I-LOC', u'B-LOC', u'B-LOC') , (u'B-ORG', u'B-LOC', u'B-LOC') , (u'O', u'I-LOC', u'B-LOC') , (u'B-PER', u'I-LOC', u'B-LOC') , (u'B-LOC', u'I-LOC', u'B-LOC') , (u'I-LOC', u'I-LOC', u'B-LOC') , (u'B-ORG', u'I-LOC', u'B-LOC') , (u'O', u'B-ORG', u'B-LOC') , (u'B-PER', u'B-ORG', u'B-LOC') , (u'B-LOC', u'B-ORG', u'B-LOC') , (u'B-ORG', u'B-ORG', u'B-LOC') , (u'I-ORG', u'B-ORG', u'B-LOC') , (u'O', u'O', u'I-LOC') , (u'B-PER', u'O', u'I-LOC') , (u'B-LOC', u'O', u'I-LOC') , (u'B-ORG', u'O', u'I-LOC') , (u'O', u'B-PER', u'I-LOC') , (u'B-PER', u'B-PER', u'I-LOC') , (u'I-PER', u'B-PER', u'I-LOC') , (u'B-LOC', u'B-PER', u'I-LOC') , (u'B-ORG', u'B-PER', u'I-LOC') , (u'O', u'B-LOC', u'I-LOC') , (u'B-PER', u'B-LOC', u'I-LOC') , (u'B-LOC', u'B-LOC', u'I-LOC') , (u'I-LOC', u'B-LOC', u'I-LOC') , (u'B-ORG', u'B-LOC', u'I-LOC') , (u'O', u'I-LOC', u'I-LOC') , (u'B-PER', u'I-LOC', u'I-LOC') , (u'B-LOC', u'I-LOC', u'I-LOC') , (u'I-LOC', u'I-LOC', u'I-LOC') , (u'B-ORG', u'I-LOC', u'I-LOC') , (u'O', u'B-ORG', u'I-LOC') , (u'B-PER', u'B-ORG', u'I-LOC') , (u'B-LOC', u'B-ORG', u'I-LOC') , (u'B-ORG', u'B-ORG', u'I-LOC') , (u'I-ORG', u'B-ORG', u'I-LOC') , (u'O', u'O', u'B-ORG') , (u'B-PER', u'O', u'B-ORG') , (u'B-LOC', u'O', u'B-ORG') , (u'B-ORG', u'O', u'B-ORG') , (u'O', u'B-PER', u'B-ORG') , (u'B-PER', u'B-PER', u'B-ORG') , (u'I-PER', u'B-PER', u'B-ORG') , (u'B-LOC', u'B-PER', u'B-ORG') , (u'B-ORG', u'B-PER', u'B-ORG') , (u'O', u'B-LOC', u'B-ORG') , (u'B-PER', u'B-LOC', u'B-ORG') , (u'B-LOC', u'B-LOC', u'B-ORG') , (u'I-LOC', u'B-LOC', u'B-ORG') , (u'B-ORG', u'B-LOC', u'B-ORG') , (u'O', u'B-ORG', u'B-ORG') , (u'B-PER', u'B-ORG', u'B-ORG') , (u'B-LOC', u'B-ORG', u'B-ORG') , (u'B-ORG', u'B-ORG', u'B-ORG') , (u'I-ORG', u'B-ORG', u'B-ORG') , (u'O', u'I-ORG', u'B-ORG') , (u'B-PER', u'I-ORG', u'B-ORG') , (u'B-LOC', u'I-ORG', u'B-ORG') , (u'B-ORG', u'I-ORG', u'B-ORG') , (u'I-ORG', u'I-ORG', u'B-ORG') , (u'O', u'O', u'I-ORG') , (u'B-PER', u'O', u'I-ORG') , (u'B-LOC', u'O', u'I-ORG') , (u'B-ORG', u'O', u'I-ORG') , (u'O', u'B-PER', u'I-ORG') , (u'B-PER', u'B-PER', u'I-ORG') , (u'I-PER', u'B-PER', u'I-ORG') , (u'B-LOC', u'B-PER', u'I-ORG') , (u'B-ORG', u'B-PER', u'I-ORG') , (u'O', u'B-LOC', u'I-ORG') , (u'B-PER', u'B-LOC', u'I-ORG') , (u'B-LOC', u'B-LOC', u'I-ORG') , (u'I-LOC', u'B-LOC', u'I-ORG') , (u'B-ORG', u'B-LOC', u'I-ORG') , (u'O', u'B-ORG', u'I-ORG') , (u'B-PER', u'B-ORG', u'I-ORG') , (u'B-LOC', u'B-ORG', u'I-ORG') , (u'B-ORG', u'B-ORG', u'I-ORG') , (u'I-ORG', u'B-ORG', u'I-ORG') , (u'O', u'I-ORG', u'I-ORG') , (u'B-PER', u'I-ORG', u'I-ORG') , (u'B-LOC', u'I-ORG', u'I-ORG') , (u'B-ORG', u'I-ORG', u'I-ORG') , (u'I-ORG', u'I-ORG', u'I-ORG'))
    '''
    triple = ((u"O", u"O", u"O"), (u"O", u"O", u"B-PER"), (u"O", u"O",
    u"B-LOC"), (u"O", u"O", u"B-ORG"), (u"O", u"B-PER", u"O"), (u"O",
    u"B-LOC", u"O"), (u"O", u"B-ORG", u"O"), (u"B-PER", u"O", u"O"), (u"B-ORG", u"O", u"O"), (u"B-LOC", u"O", u"O"), (u"O", u"B-PER", u"I-PER"), (u"O", u"B-LOC", u"I-LOC"), (u"O", u"B-ORG",
    u"I-ORG"), (u"B-PER", u"I-PER", u"I-PER"), (u"B-LOC", u"I-LOC", u"I-LOC"), (u"B-ORG", u"I-ORG", u"I-ORG"), (u"B-PER", u"I-PER", u"O"), (u"B-LOC", u"I-LOC",
    u"O"), (u"B-ORG", u"I-ORG", u"O"), (u"B-PER", u"I-PER", u"B-LOC"), (u"B-LOC", u"I-LOC", u"B-PER"), (u"B-ORG", u"I-ORG",
    u"B-PER"), (u"B-PER", u"I-PER", u"B-ORG"), (u"B-LOC", u"I-LOC", u"B-ORG"), (u"B-ORG", u"I-ORG", u"B-LOC"), (u"O", u"B-PER", u"B-ORG"), (u"O", u"B-LOC",
    u"B-ORG"), (u"O", u"B-PER", u"B-LOC"), (u"O", u"B-LOC", u"B-ORG"))
    '''
    #bi = set([(u"B-PER", u"I-PER"), (u"B-LOC", u"I-LOC"), (u"B-ORG", u"I-ORG")])
    dp = []
    feature = []
    
    for i in range(len(sentence)):
        dp.append({})
        feature.append({})
        if(i < 2):
            for tri in triple:
                dp[i][tri] = (0, "O")
            '''
            for tag1 in tags:
                for tag2 in tags:
                    for tag3 in tags:
                        dp[i][(tag1, tag2, tag3)] = (0, "O")
            '''
            continue;
        #print dp
        for tri in triple:
            tmp_f = cal_feature(i, sentence, tri, opt)
            feature[i][tri] = tmp_f
            sum_feature = sum_up_features(tmp_f, params, opt["charac"][sentence[i]], tags.index(tri[0]))
            #max_feature = dp[i - 1][(tri[1], tri[2], u"O")][0]
            #max_tag = u"O"
            max_feature = float('-Inf')
            max_tag = "null"
            for tag4 in tags:
                new_tri = (tri[1], tri[2], tag4)
                if(not new_tri in triple):
                    continue;
                if(dp[i - 1][(tri[1], tri[2], tag4)][0] > max_feature):
                    max_feature = dp[i - 1][(tri[1], tri[2], tag4)][0]
                    max_tag = tag4
            final_feature = max_feature + sum_feature
            dp[i][tri] = (final_feature, max_tag)
        '''
        for tag1 in tags: # The current word
            for tag2 in tags: # The previous word
                if(tag1 == u"I-PER" or tag1 == u"I-LOC" or tag1 == u"I-ORG"):
                    if(not (tag2, tag1) in bi):
                        continue;
                for tag3 in tags: # The word two back
                    
                    print "Tags: ",
                    print tag1,
                    print tag2,
                    print tag3,
                    
                    if(tag2 == u"I-PER" or tag2 == u"I-LOC" or tag2 == u"I-ORG"):
                        if(not (tag3, tag2) in bi):
                            continue;


                    
                    tmp_f = cal_feature(i, sentence, (tag1, tag2, tag3), opt)
                    feature[i][(tag1, tag2, tag3)] = tmp_f
                    
                    print "Features: ",
                    print tmp_f
                    
                    sum_feature = sum_up_features(tmp_f, params)
                    max_feature = dp[i - 1][(tag2, tag3, u"O")][0]
                    max_tag = u"O"
                    for tag4 in tags:
                        if(dp[i - 1][(tag2, tag3, tag4)][0] > max_feature):
                            max_feature = dp[i - 1][(tag2, tag3, tag4)][0]
                            max_tag = tag4
                    final_feature = max_feature + sum_feature
                    dp[i][(tag1, tag2, tag3)] = (final_feature, max_tag)
        '''
    i = len(sentence) - 1
    u = sorted(dp[i].items(), key = lambda q:q[1][0], reverse = True)
    print sentence[-3], sentence[-2], sentence[-1]
    print u[0]
    print u[-1]
    cur_tag = []
    u = u[0]
    
    while(i > 1):
        tri_tag = u[0]
        cur_tag.append(u[0][0])
        new_tri_tag = (u[0][1], u[0][2], u[1][1])
        
        i = i - 1
        u = (new_tri_tag, dp[i][new_tri_tag])
    cur_tag.append(u"O")
    cur_tag.append(u"O")
    cur_tag.reverse()
    #print cur_tag
    if(cur_tag[2] == u"I-PER"):
        cur_tag[2] = u"B-PER"
    if(cur_tag[2] == u"I-LOC"):
        cur_tag[2] = u"B-LOC"
    if(cur_tag[2] == u"I-ORG"):
        cur_tag[2] = u"B-ORG"
    
    return (cur_tag, feature)



def viterbi_bi(sentence, params, opt):
    tags = (u"O", u"B-PER", u"I-PER", u"B-LOC", u"I-LOC", u"B-ORG", u"I-ORG")

    bi = ((u'B-PER', u'I-PER'), (u'B-PER', u'B-PER'), (u'B-LOC', u'I-LOC'), (u'B-LOC', u'I-ORG'), (u'B-ORG', u'O'), (u'O', u'B-PER'), (u'B-ORG', u'I-LOC'), (u'O', u'B-ORG'), (u'I-ORG', u'I-ORG'), (u'B-ORG', u'B-ORG'), (u'I-ORG', u'B-ORG'), (u'B-PER', u'I-ORG'), (u'B-PER', u'I-LOC'), (u'B-ORG', u'I-PER'), (u'I-PER', u'B-PER'), (u'O', u'O'), (u'O', u'I-ORG'), (u'B-LOC', u'I-PER'), (u'B-LOC', u'B-LOC'), (u'B-ORG', u'B-LOC'), (u'I-LOC', u'B-LOC'), (u'O', u'I-PER'), (u'O', u'I-LOC'), (u'B-PER', u'O'), (u'B-LOC', u'O'), (u'O', u'B-LOC'), (u'I-LOC', u'I-LOC'), (u'I-PER', u'I-PER'), (u'B-ORG', u'I-ORG'))
    dp = []
    feature = []
    sentence.extend([u"", u""])
    for i in range(len(sentence) - 2):
        dp.append({})
        feature.append({})
        if(i < 2):
            for b in bi:
                dp[i][b] = (0, "O")
            '''
            for tag1 in tags:
                for tag2 in tags:
                    for tag3 in tags:
                        dp[i][(tag1, tag2, tag3)] = (0, "O")
            '''
            continue;
        #print dp
        for b in bi:
            tmp_f = cal_feature(i, sentence, b, opt)
            feature[i][b] = tmp_f
            sum_feature = sum_up_features(tmp_f, params, opt["charac"], tags.index(b[0]), i, sentence, opt["biword"])
            #max_feature = dp[i - 1][(tri[1], tri[2], u"O")][0]
            #max_tag = u"O"
            max_feature = float('-Inf')
            max_tag = "null"
            for tag4 in tags:
                new_b = (b[1], tag4)
                if(not new_b in bi):
                    continue;
                if(dp[i - 1][(b[1], tag4)][0] > max_feature):
                    max_feature = dp[i - 1][(b[1], tag4)][0]
                    max_tag = tag4
            final_feature = max_feature + sum_feature
            dp[i][b] = (final_feature, max_tag)
        '''
        for tag1 in tags: # The current word
            for tag2 in tags: # The previous word
                if(tag1 == u"I-PER" or tag1 == u"I-LOC" or tag1 == u"I-ORG"):
                    if(not (tag2, tag1) in bi):
                        continue;
                for tag3 in tags: # The word two back
                    
                    print "Tags: ",
                    print tag1,
                    print tag2,
                    print tag3,
                    
                    if(tag2 == u"I-PER" or tag2 == u"I-LOC" or tag2 == u"I-ORG"):
                        if(not (tag3, tag2) in bi):
                            continue;


                    
                    tmp_f = cal_feature(i, sentence, (tag1, tag2, tag3), opt)
                    feature[i][(tag1, tag2, tag3)] = tmp_f
                    
                    print "Features: ",
                    print tmp_f
                    
                    sum_feature = sum_up_features(tmp_f, params)
                    max_feature = dp[i - 1][(tag2, tag3, u"O")][0]
                    max_tag = u"O"
                    for tag4 in tags:
                        if(dp[i - 1][(tag2, tag3, tag4)][0] > max_feature):
                            max_feature = dp[i - 1][(tag2, tag3, tag4)][0]
                            max_tag = tag4
                    final_feature = max_feature + sum_feature
                    dp[i][(tag1, tag2, tag3)] = (final_feature, max_tag)
        '''
    sentence.pop()
    sentence.pop()
    i = len(sentence) - 1
    u = sorted(dp[i].items(), key = lambda q:q[1][0], reverse = True)
    #print sentence[-3], sentence[-2], sentence[-1]
    #print u[0]
    #print u[-1]
    cur_tag = []
    u = u[0]
    
    while(i > 1):
        tri_tag = u[0]
        cur_tag.append(u[0][0])
        new_b_tag = (u[0][1],  u[1][1])
        
        i = i - 1
        u = (new_b_tag, dp[i][new_b_tag])
    cur_tag.append(u"O")
    cur_tag.append(u"O")
    cur_tag.reverse()
    #print cur_tag
    if(cur_tag[2] == u"I-PER"):
        cur_tag[2] = u"B-PER"
    if(cur_tag[2] == u"I-LOC"):
        cur_tag[2] = u"B-LOC"
    if(cur_tag[2] == u"I-ORG"):
        cur_tag[2] = u"B-ORG"
    
    return (cur_tag, feature)

def sum_up_features(features, params, word, v, i, sentence, biword):
    sum = 0
    for u in range(i-2, i + 3):
        if(sentence[u] in word):
            sum += params[word[sentence[u]] + v * 4361 + (u - i + 2) * 4361 * 7]
    for u in range(i - 2, i + 2):
        if((sentence[u], sentence[u + 1]) in biword):
           sum += params[biword[(sentence[u], sentence[u + 1])] + 5 * 7 * 4361 + (u - i + 2) * 89148 * 7 + v * 89148]
    
    for i in range(len(features)):
        #sum += features[i] * params[i]
        sum += params[i + 4361 * 7 * 5 + 4 * 7 * 89148]

    return sum
            


