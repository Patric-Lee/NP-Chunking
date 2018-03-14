def triple():
    '''
    tags = (u"O", u"B-PER", u"I-PER", u"B-LOC", u"I-LOC", u"B-ORG", u"I-ORG")
    i = 0
    for tag1 in tags:
        for tag2 in tags:
            if(tag2 == u"I-PER" and tag1 != u"B-PER" and tag1 != u"I-PER" or tag2 == u"I-LOC" and tag1 != u"B-LOC" and tag1 != u"I-LOC"or tag2 == u"I-ORG" and tag1 != u"B-ORG" and tag1 != u"I-ORG"):
                continue;
            for tag3 in tags:
                if(tag3 == u"I-PER" and tag2 != u"B-PER" and tag2 != u"I-PER" or tag3 == u"I-LOC" and tag2 != u"B-LOC" and tag2 != u"I-LOC"or tag3 == u"I-ORG" and tag2 != u"B-ORG" and tag2 != u"I-ORG"):
                    continue;
                i = i + 1
                print (tag3, tag2, tag1),
                print ",",
                #print i
    '''
    tags = (u"O", u"PER", u"LOC", u"ORG")
    for tag1 in tags:
        for tag2 in tags:
            for tag3 in tags:
                if(tag3 != tag2 and tag3!=u"O" and tag2 != u"O"):
                    continue;
                if(tag1 != tag2 and tag1!=u"O" and tag2 != u"O"):
                    continue;
                print (tag3, tag2, tag1),
                print ",",

triple()
