#!/usr/local/bin/python
import random

def roller(nrange):
    roller = random.randint(1,nrange)
    return roller

def dictionary(entropy):
    data =[['01','A','A','I','A','A','O','Z','FF','HH'],['02','B','B','I','B','B','P','Z','FF','HH'],['03','B','B','J','C','C','Q','AA','FF','II'],['04','C','C','J','D','D','Q','BB','GG','II'],['05','C','C','J','E','E','R','BB','HH','II'],['06','D','D','K','F','E','S','CC','II','II'],['07','D','D','K','G','F','T','CC','II','JJ'],['08','E','E','K','H','G','T','DD','JJ','JJ'],['09','E','E','K','I','H','U','EE','JJ','JJ'],['10','E','E','K','J','L','U','EE','JJ','JJ'],['11','F','F','K','K','M','V','FF','KK','KK'],['12','F','F','L','L','N','W','FF','KK','KK'],['13','G','G','L','M','O','X','GG','KK','KK'],['14','G','G','M','N','O','Y','HH','LL','KK'],['15','H','H','M','O','P','Y','II','LL','LL'],['16','H','H','N','O','Q','Z','II','LL','LL'],['17','I','I','N','P','Q','AA','JJ','MM','LL'],['18','I','I','O','Q','R','BB','JJ','MM','LL'],['19','J','J','O','Q','S','CC','KK','MM','MM'],['20','J','J','O','R','T','CC','KK','MM','MM'],['21','J','J','P','S','T','DD','LL','NN','MM'],['22','J','K','P','T','U','EE','LL','NN','MM'],['23','K','K','Q','T','U','FF','MM','OO','MM'],['24','K','K','Q','U','V','FF','MM','PP','MM'],['25','K','K','R','U','W','GG','MM','QQ','NN'],['26','K','L','R','V','X','HH','NN','RR','NN'],['27','L','L','S','W','X','II','NN','SS','NN'],['28','L','M','S','X','Y','II','OO','SS','OO'],['29','M','M','T','X','Z','JJ','PP','SS','PP'],['30','M','N','T','Y','AA','JJ','QQ','TT','QQ'],['31','N','N','U','Z','BB','KK','RR','WW','RR'],['32','N','O','U','AA','CC','KK','SS','XX','SS'],['33','O','O','U','BB','CC','LL','SS','XX','SS'],['34','O','P','U','CC','DD','LL','TT','XX','SS'],['35','P','P','U','CC','EE','MM','UU','YY','SS'],['36','P','Q','U','DD','FF','MM','UU','YY','TT'],['37','Q','Q','V','EE','GG','MM','VV','YY','XX'],['38','Q','Q','V','FF','HH','NN','VV','BBB','XX'],['39','Q','R','W','GG','II','OO','WW','BBB','XX'],['40','Q','R','W','HH','JJ','PP','XX','BBB','XX'],['41','R','S','X','II','KK','QQ','XX','BBB','YY'],['42','R','S','X','JJ','LL','RR','YY','CCC','YY'],['43','S','T','Y','KK','MM','SS','YY','CCC','YY'],['44','S','T','Z','LL','MM','SS','ZZ','CCC','YY'],['45','T','U','Z','MM','NN','TT','ZZ','DDD','CCC'],['46','T','U','AA','MM','OO','UU','AAA','DDD','CCC'],['47','T','U','BB','NN','PP','VV','AAA','LLL','CCC'],['48','U','U','CC','OO','QQ','WW','BBB','LLL','CCC'],['49','U','V','CC','PP','RR','XX','BBB','MMM','CCC'],['50','U','V','DD','QQ','SS','XX','BBB','MMM','CCC'],['51','U','W','DD','RR','TT','YY','CCC','NNN','DDD'],['52','V','W','EE','SS','UU','YY','CCC','NNN','DDD'],['53','V','X','FF','TT','UU','ZZ','CCC','OOO','PPP'],['54','W','X','FF','UU','VV','ZZ','DDD','OOO','PPP'],['55','W','Y','FF','UU','VV','AAA','DDD','OOO','PPP'],['56','W','Y','GG','VV','WW','BBB','HHH','OOO','PPP'],['57','X','Z','HH','VV','XX','BBB','III','PPP','QQQ'],['58','X','Z','HH','WW','YY','CCC','JJJ','PPP','QQQ'],['59','Y','Z','II','XX','ZZ','CCC','JJJ','PPP','QQQ'],['60','Y','AA','II','YY','ZZ','CCC','JJJ','PPP','QQQ'],['61','Z','BB','JJ','ZZ','AAA','DDD','JJJ','QQQ','RRR'],['62','Z','CC','JJ','ZZ','BBB','DDD','KKK','QQQ','RRR'],['63','Z','CC','JJ','AAA','BBB','EEE','KKK','QQQ','RRR'],['64','AA','CC','KK','BBB','CCC','FFF','LLL','QQQ','SSS'],['65','BB','DD','KK','BBB','CCC','GGG','LLL','RRR','SSS'],['66','BB','DD','LL','CCC','DDD','HHH','MMM','RRR','SSS'],['67','CC','EE','LL','CCC','EEE','III','MMM','RRR','SSS'],['68','CC','FF','MM','DDD','FFF','JJJ','NNN','SSS','TTT'],['69','CC','FF','MM','EEE','GGG','JJJ','NNN','SSS','TTT'],['70','DD','FF','NN','GGG','HHH','JJJ','OOO','SSS','TTT'],['71','DD','GG','OO','HHH','III','JJJ','OOO','SSS','TTT'],['72','EE','HH','OO','III','JJJ','KKK','OOO','TTT','UUU'],['73','EE','HH','PP','JJJ','JJJ','KKK','PPP','TTT','UUU'],['74','FF','II','QQ','JJJ','KKK','LLL','PPP','TTT','UUU'],['75','FF','II','QQ','KKK','LLL','MMM','PPP','TTT','UUU'],['76','FF','JJ','RR','LLL','MMM','NNN','QQQ','UUU','VVV'],['77','FF','JJ','RR','MMM','NNN','OOO','QQQ','UUU','VVV'],['78','GG','JJ','SS','NNN','OOO','OOO','QQQ','UUU','VVV'],['79','HH','KK','TT','OOO','OOO','PPP','RRR','VVV','VVV'],['80','HH','KK','TT','PPP','PPP','PPP','RRR','VVV','WWW'],['81','II','LL','UU','PPP','PPP','QQQ','SSS','VVV','WWW'],['82','II','MM','UU','QQQ','QQQ','QQQ','SSS','VVV','WWW'],['83','JJ','MM','VV','QQQ','QQQ','RRR','SSS','WWW','WWW'],['84','JJ','NN','VV','RRR','RRR','SSS','TTT','WWW','XXX'],['85','JJ','OO','WW','SSS','SSS','SSS','TTT','WWW','XXX'],['86','KK','PP','XX','SSS','SSS','TTT','TTT','WWW','XXX'],['87','KK','QQ','XX','TTT','TTT','TTT','UUU','XXX','XXX'],['88','LL','QQ','YY','TTT','TTT','UUU','UUU','XXX','YYY'],['89','MM','RR','YY','UUU','UUU','UUU','VVV','XXX','YYY'],['90','MM','RR','ZZ','VVV','VVV','VVV','VVV','XXX','YYY'],['91','NN','SS','ZZ','VVV','VVV','VVV','WWW','YYY','YYY'],['92','OO','TT','AAA','WWW','WWW','WWW','WWW','YYY','ZZZ'],['93','PP','UU','AAA','WWW','WWW','WWW','XXX','YYY','ZZZ'],['94','QQ','UU','BBB','XXX','XXX','XXX','XXX','YYY','ZZZ'],['95','QQ','VV','BBB','XXX','XXX','XXX','YYY','ZZZ','ZZZ'],['96','RR','VV','CCC','YYY','YYY','YYY','YYY','ZZZ','AAAA'],['97','RR','WW','CCC','YYY','YYY','YYY','ZZZ','ZZZ','AAAA'],['98','SS','XX','DDD','ZZZ','ZZZ','ZZZ','ZZZ','AAAA','AAAA'],['99','TT','YY','DDD','AAAA','AAAA','AAAA','AAAA','AAAA','AAAA'],['00','RollX2','RollX2','RollX2','RollX2','RollX2','RollX2','RollX2','RollX2','RollX2']]
    dataset = data[entropy]
    return dataset

def main():
    timeandplace=prettygui()
    entropy=roller(100)
    dataset = dictionary(entropy)
    print dataset[int(timeandplace)]

def prettygui():
    #Yeah not yet...
    print "Select:\n"
    print "1) Corporate Zone: Daytime"
    print "2) Corporate Zone: Evening"
    print "3) Corporate Zone: Night"
    print "4) Moderate Zone: Daytime"
    print "5) Moderate Zone: Evening"
    print "6) Moderate Zone: Night"
    print "7) Combat Zone: Daytime"
    print "8) Combat Zone: Evening"
    print "9) Combat Zone: Night"
    gui=raw_input()
    return gui


main()
