#!/usr/local/bin/python
# -*- coding: utf-8 -*-

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
    details=dataset[int(timeandplace)]
    detailencounter=encounterdetail(details)
    print detailencounter


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


def encounterdetail(zone):
    entropyten=roller(10)

    if zone == "A":
        encounter = "Lost Child"
        if 1 <= entropyten <= 3:
             encountermodifier = " Wandering aimlessly."
        if 4 <= entropyten <= 6:
             encountermodifier = " Asks for the PCs’ help."
        if 7 <= entropyten <= 9:
             encountermodifier = " Inadvertently grabs a PC’s hand."
        if 10 <= entropyten <= 10:
             encountermodifier = " Gets picked up by the nice man in the big black unmarked car."
    if zone == "B":
        encounter = "Mall Rats (1d4+1)"
        if 1 <= entropyten <= 2:
             encountermodifier = " Shopping till they drop."
        if 3 <= entropyten <= 4:
             encountermodifier = " Boisterously comparing the newest fashions (actually pretty ugly stuff)."
        if 5 <= entropyten <= 6:
             encountermodifier = " Shoplifting."
        if 7 <= entropyten <= 8:
             encountermodifier = " Playing mall tag."
        if 9 <= entropyten <= 9:
             encountermodifier = " Attempting to pickpocket CredStiks."
        if 10 <= entropyten <= 10:
             encountermodifier = " Attempting to pickpocket a PC’s CredStik."
    if zone == "C":
        encounter = "Priest"
        if 1 <= entropyten <= 5:
             encountermodifier = " On their way to the church."
        if 6 <= entropyten <= 8:
             encountermodifier = " Collecting donations."
        if 9 <= entropyten <= 9:
             encountermodifier = " Performing random blessings."
        if 10 <= entropyten <= 10:
             encountermodifier = " Proclaims the end is near and condemns the PCs to Hell."
    if zone == "D":
        encounter = "Rabbi"
        if 1 <= entropyten <= 6:
             encountermodifier = " On their way to the synagogue."
        if 7 <= entropyten <= 8:
             encountermodifier = " Stopping for a bite to eat"
        if 9 <= entropyten <= 10:
             encountermodifier = " Consoling a grieving woman."
    if zone == "E":
        encounter = "VideoVangelist"
        if 1 <= entropyten <= 5:
             encountermodifier = " Preaching the 'Beaver' and 'Brady' scriptures."
        if 6 <= entropyten <= 7:
             encountermodifier = " Handing out pamphlets."
        if 8 <= entropyten <= 8:
             encountermodifier = " Handing out pocket TVs (probably stolen). One per customer, please."
        if 9 <= entropyten <= 10:
             encountermodifier = " Calls the PCs heretics!"
    if zone == "F":
        encounter = "Buddhists (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Meditating on a park bench."
        if 4 <= entropyten <= 8:
             encountermodifier = " On their way to the temple."
        if 9 <= entropyten <= 10:
             encountermodifier = " Leading a public meditation."
    if zone == "G":
        encounter = "Mormons (2)"
        if 1 <= entropyten <= 7:
             encountermodifier = " Spreading the word door-to- door."
        if 8 <= entropyten <= 9:
             encountermodifier = " Stopping for lunch."
        if 10 <= entropyten <= 10:
             encountermodifier = " Being harassed by angry civilian."
    if zone == "H":
        encounter = "Children Playing (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " In an alley."
        if 4 <= entropyten <= 6:
             encountermodifier = " In the street."
        if 7 <= entropyten <= 8:
             encountermodifier = " With dangerous objects."
        if 9 <= entropyten <= 10:
             encountermodifier = " On the PCs’ vehicle."
    if zone == "I":
        encounter = "Bicycle Courier"
        if 1 <= entropyten <= 3:
             encountermodifier = " Stopped for a snack."
        if 4 <= entropyten <= 7:
             encountermodifier = " On a run and just barely missed the PCs."
        if 8 <= entropyten <= 9:
             encountermodifier = " Just plowed into somebody. Bike parts everywhere!"
        if 10 <= entropyten <= 10:
             encountermodifier = " Just plowed into a PC."
    if zone == "J":
        encounter = "Corporates (1d4+1)"
        if 1 <= entropyten <= 4:
             encountermodifier = " On break. Probably at the ShrimpChip Noodle BarTM."
        if 5 <= entropyten <= 8:
             encountermodifier = " Discussing some new business (technology/contracts/take overs/etc.) over drinks."
        if 9 <= entropyten <= 10:
             encountermodifier = " Looking for some protection."
    if zone == "K":
        encounter = "Corporate Security (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " On their break and going to the ShrimpChip Noodle BarTM."
        if 4 <= entropyten <= 5:
             encountermodifier = " Standing post."
        if 6 <= entropyten <= 7:
             encountermodifier = " Providing protection for a big suit. Don't ask."
        if 8 <= entropyten <= 9:
             encountermodifier = " Checking everybody's papers."
        if 10 <= entropyten <= 10:
             encountermodifier = " Bored and decide to pin something on the PCs."
    if zone == "L":
        encounter = "Rocker"
        if 1 <= entropyten <= 3:
             encountermodifier = " Hard on their luck and trying to write songs while looking for a job."
        if 4 <= entropyten <= 5:
             encountermodifier = " Signing autographs."
        if 6 <= entropyten <= 7:
             encountermodifier = " Making a PR move by handing out tickets to the next show."
        if 8 <= entropyten <= 10:
             encountermodifier = " Sends their bodyguards to deal with 'that tough crowd over there.'"
    if zone == "M":
        encounter = "SimStim Star"
        if 1 <= entropyten <= 5:
             encountermodifier = " Making a quick escape from the crowds."
        if 6 <= entropyten <= 8:
             encountermodifier = " Signing autographs."
        if 9 <= entropyten <= 10:
             encountermodifier = " Sends their bodyguards to deal with 'that tough crowd over there.' "
    if zone == "N":
        encounter = "Religious Fanatic complete with robes"
        if 1 <= entropyten <= 4:
             encountermodifier = " Standing on a “soapbox” and has a small crowd gathering."
        if 5 <= entropyten <= 7:
             encountermodifier = " Wildly preaching to himself."
        if 8 <= entropyten <= 10:
             encountermodifier = " Attempts to coerce the PCs into believing."
    if zone == "O":
        encounter = "College Students (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Discussing the newest technologies."
        if 4 <= entropyten <= 6:
             encountermodifier = " Scoping for partners for the night."
        if 7 <= entropyten <= 9:
             encountermodifier = " Drunk or looking for a place to get drunk."
        if 10 <= entropyten <= 10:
             encountermodifier = " Being harassed by a local gang."
    if zone == "P":
        encounter = "Mnemonic Courier"
        if 1 <= entropyten <= 3:
             encountermodifier = " Looking for a contract."
        if 4 <= entropyten <= 6:
             encountermodifier = " Taking a break and enjoying a drink."
        if 7 <= entropyten <= 9:
             encountermodifier = " On the job and would rather not be bothered."
        if 10 <= entropyten <= 10:
             encountermodifier = " Being chased by a bunch of guys who want what's in their skull."
    if zone == "Q":
        encounter = "Techies (2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " On break."
        if 5 <= entropyten <= 7:
             encountermodifier = " Discussing new technology over a meal."
        if 8 <= entropyten <= 10:
             encountermodifier = " Carefully dissecting some bit of equipment."
    if zone == "R":
        encounter = "Medic"
        if 1 <= entropyten <= 3:
             encountermodifier = " Looking for a job."
        if 4 <= entropyten <= 7:
             encountermodifier = " Taking a break."
        if 9 <= entropyten <= 10:
             encountermodifier = " Working on some unfortunate bystander."
    if zone == "S":
        encounter = "Pilot"
        if 1 <= entropyten <= 4:
             encountermodifier = " Looking for a job."
        if 6 <= entropyten <= 8:
             encountermodifier = " Slightly drunk and spinning tall tales."
        if 9 <= entropyten <= 10:
             encountermodifier = " Heavily sedated with alcohol."
    if zone == "T":
        encounter = "Military Personnel (1d6)"
        if 1 <= entropyten <= 4:
             encountermodifier = " On leave and in civilian clothes."
        if 5 <= entropyten <= 7:
             encountermodifier = " On leave for a few hours."
        if 8 <= entropyten <= 9:
             encountermodifier = " Looking for somebody."
        if 10 <= entropyten <= 10:
             encountermodifier = " Drunk and looking for a fight."
    if zone == "U":
        encounter = "Corporate Police (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Keeping the peace."
        if 4 <= entropyten <= 6:
             encountermodifier = " Randomly checking to see if papers are in order."
        if 7 <= entropyten <= 7:
             encountermodifier = " Knocking down someone's door."
        if 8 <= entropyten <= 9:
             encountermodifier = " Politely ask the PCs to leave the area."
        if 10 <= entropyten <= 10:
             encountermodifier = " Decide the PCs don't belong in this zone and have itchy trigger fingers."
    if zone == "V":
        encounter = "Hacker"
        if 1 <= entropyten <= 3:
             encountermodifier = " Just hanging out."
        if 4 <= entropyten <= 6:
             encountermodifier = " Looking for the next gig."
        if 7 <= entropyten <= 9:
             encountermodifier = " Scoping out some intel."
        if 10 <= entropyten <= 10:
             encountermodifier = " Jacked in and probably wreaking havoc."
    if zone == "W":
        encounter = "Body Guard"
        if 1 <= entropyten <= 3:
             encountermodifier = " Off duty and looking for a job."
        if 4 <= entropyten <= 6:
             encountermodifier = " Accompanying a big suit. Don't ask."
        if 7 <= entropyten <= 9:
             encountermodifier = " Accompanying a gorgeous SimStim star or Rocker. Don't get too close!"
        if 10 <= entropyten <= 10:
             encountermodifier = " Has just lost a client the hard way and is a little irritable."
    if zone == "X":
        encounter = "Exotic"
        if 1 <= entropyten <= 3:
             encountermodifier = " Is showing off their newest surgery to their friends."
        if 4 <= entropyten <= 6:
             encountermodifier = " Is trying to pick up another exotic."
        if 7 <= entropyten <= 9:
             encountermodifier = " Is trying their hand at prostitution."
        if 10 <= entropyten <= 10:
             encountermodifier = " Will beat the snot out of the PCs if they make any comment."
    if zone == "Y":
        encounter = "Neutral Crowd (3d4)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Just mulling about."
        if 4 <= entropyten <= 5:
             encountermodifier = " Waiting for a bus, train, or maglev tram."
        if 6 <= entropyten <= 8:
             encountermodifier = " Shopping."
        if 9 <= entropyten <= 10:
             encountermodifier = " Gathering for a major entertainment event (movie, concert, sports, etc.)"
    if zone == "Z":
        encounter = "Riot Police (1d4+2)"
        if 1 <= entropyten <= 5:
             encountermodifier = " All suited up and heading towards a dispute."
        if 6 <= entropyten <= 8:
             encountermodifier = " In the process of controlling some unruly shoppers."
        if 9 <= entropyten <= 10:
             encountermodifier = " Smack dab in the middle of a firefight with an ugly crowd."
    if zone == "AA":
        encounter = "Government Petitioner"
        if 1 <= entropyten <= 7:
             encountermodifier = " Is asking for signatures."
        if 8 <= entropyten <= 9:
             encountermodifier = " Will slander the PCs’ choice of political party."
        if 10 <= entropyten <= 10:
             encountermodifier = " Doesn't like the PCs and will call the nearest authorities."
    if zone == "BB":
        encounter = "Picketers (3d6) protesting against:"
        if 1 <= entropyten <= 2:
             encountermodifier = " Unfair government."
        if 3 <= entropyten <= 4:
             encountermodifier = " Unfair taxes."
        if 5 <= entropyten <= 6:
             encountermodifier = " An unfair corporation."
        if 7 <= entropyten <= 8:
             encountermodifier = " Unfair wages or standard of living."
        if 9 <= entropyten <= 10:
             encountermodifier = " Discrimination."
    if zone == "CC":
        encounter = "Taxi Cab Driver"
        if 1 <= entropyten <= 5:
             encountermodifier = " Driving a fare."
        if 6 <= entropyten <= 9:
             encountermodifier = " Looking for a fare."
        if 10 <= entropyten <= 10:
             encountermodifier = " Has just been in an accident and is having a dispute with the other driver."
    if zone == "DD":
        encounter = "Private Investigator"
        if 1 <= entropyten <= 4:
             encountermodifier = " Taking some time off."
        if 5 <= entropyten <= 6:
             encountermodifier = " Looking for a job."
        if 7 <= entropyten <= 8:
             encountermodifier = " Following a lead."
        if 9 <= entropyten <= 10:
             encountermodifier = " Seems to be following the PCs."
    if zone == "EE":
        encounter = "Construction Workers (1d4+2)"
        if 1 <= entropyten <= 3:
             encountermodifier = " On a coffee break."
        if 4 <= entropyten <= 8:
             encountermodifier = " Working."
        if 9 <= entropyten <= 10:
             encountermodifier = " Hootin' and hollarin' at the attractive members of the PC group."
    if zone == "FF":
        encounter = "Media Team"
        if 1 <= entropyten <= 2:
             encountermodifier = " Taking a break."
        if 3 <= entropyten <= 4:
             encountermodifier = " Doing random interviews."
        if 5 <= entropyten <= 6:
             encountermodifier = " Working on a major story."
        if 7 <= entropyten <= 8:
             encountermodifier = " Their story subject opens fire on them."
        if 9 <= entropyten <= 10:
             encountermodifier = " Has decided the PCs are a worthy story to follow."
    if zone == "GG":
        encounter = "Car Accident (1d4)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Minor. The drivers are exchanging info."
        if 5 <= entropyten <= 6:
             encountermodifier = " Moderate. They could use some help. Police are on the way."
        if 7 <= entropyten <= 8:
             encountermodifier = " Major. Traffic is held up. Police and Trauma Team everywhere."
        if 9 <= entropyten <= 10:
             encountermodifier = " Extreme. Fatal. Looting has ensued from all the chaos."
    if zone == "HH":
        encounter = "Construction"
        if 1 <= entropyten <= 4:
             encountermodifier = " Typical annoyance."
        if 5 <= entropyten <= 7:
             encountermodifier = " Holding up traffic."
        if 8 <= entropyten <= 10:
             encountermodifier = " Completely blocks off the street."
    if zone == "II":
        encounter = "Religious Crazy complete with robes or completely naked"
        if 1 <= entropyten <= 3:
             encountermodifier = "'The end is nigh!'"
        if 4 <= entropyten <= 6:
             encountermodifier = " 'Repent sinners!'"
        if 7 <= entropyten <= 10:
             encountermodifier = " 'I condemn you to Hell!'"
    if zone == "JJ":
        encounter = "Trauma Team"
        if 1 <= entropyten <= 4:
             encountermodifier = " On break and are checking their gear."
        if 5 <= entropyten <= 7:
             encountermodifier = " En route to a contract."
        if 8 <= entropyten <= 10:
             encountermodifier = " Fulfilling a contract and decide the PCs are part of the problem."
    if zone == "KK":
        encounter = "Bullies (1d4+1)"
        if 1 <= entropyten <= 2:
             encountermodifier = " Are harassing some schoolkids."
        if 3 <= entropyten <= 4:
             encountermodifier = " Are harassing some women."
        if 5 <= entropyten <= 6:
             encountermodifier = " Are harassing some corporates."
        if 7 <= entropyten <= 10:
             encountermodifier = " Are harassing the PCs."
    if zone == "LL":
        encounter = "Stray Cat"
        if 1 <= entropyten <= 4:
             encountermodifier = " Slinking down an alley."
        if 5 <= entropyten <= 5:
             encountermodifier = " Slinks up to you looking for some affection."
        if 6 <= entropyten <= 8:
             encountermodifier = " Dumpster diving for food scraps."
        if 9 <= entropyten <= 9:
             encountermodifier = " Fighting another cat over food scraps. Fur everywhere!"
        if 10 <= entropyten <= 10:
             encountermodifier = " Rabid and decides to attack the nearest living thing."
    if zone == "MM":
        encounter = "Drug Addict"
        if 1 <= entropyten <= 3:
             encountermodifier = " Tripping in the middle of the street."
        if 4 <= entropyten <= 6:
             encountermodifier = " Begs for some pocket change."
        if 7 <= entropyten <= 9:
             encountermodifier = " Passed out."
        if 10 <= entropyten <= 10:
             encountermodifier = " Robs the PCs at gunpoint to feed their habit."
    if zone == "NN":
        encounter = "Riot (3d6)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Fighting over food stamps (or something else)."
        if 4 <= entropyten <= 6:
             encountermodifier = " Trying to get a glimpse of their favorite Rocker or SimStim star."
        if 7 <= entropyten <= 10:
             encountermodifier = " Being assaulted by riot police."
    if zone == "OO":
        encounter = "C-SWAT (1d4+1)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Preparing to go on a run."
        if 5 <= entropyten <= 7:
             encountermodifier = " On the way or have opened fire on a cyberpsycho - STAY CLEAR!"
        if 8 <= entropyten <= 10:
             encountermodifier = " Have decided the PCs are a threat to society."
    if zone == "PP":
        encounter = "CyberPsycho"
        if 1 <= entropyten <= 3:
             encountermodifier = " Flexing their cyberware in front of some chrome beauties."
        if 4 <= entropyten <= 4:
             encountermodifier = " Taking the engine of a car out - with their bare hands."
        if 5 <= entropyten <= 5:
             encountermodifier = " Putting signposts and street lamps through mailboxes."
        if 6 <= entropyten <= 6:
             encountermodifier = " Trying to get to the juicy insides of a corner DataTerm."
        if 7 <= entropyten <= 7:
             encountermodifier = " Trying to stomp on a stray dog."
        if 8 <= entropyten <= 8:
             encountermodifier = " Crouched in the fetal position in the middle of what's left of a motorcycle, car, or dumpster."
        if 9 <= entropyten <= 9:
             encountermodifier = " Decides to squish a PC’s head."
        if 10 <= entropyten <= 10:
             encountermodifier = " Being assaulted by C-SWAT. Not fun."
    if zone == "QQ":
        encounter = "Solo"
        if 1 <= entropyten <= 4:
             encountermodifier = " Looking for a contract."
        if 5 <= entropyten <= 7:
             encountermodifier = " Been hanging out at the bar a while and their judgment is impaired."
        if 8 <= entropyten <= 9:
             encountermodifier = " Wants to prove he's better than one of the PCs."
        if 10 <= entropyten <= 10:
             encountermodifier = " In the middle of an op and has no qualms about terminating witnesses."
    if zone == "RR":
        encounter = "Mercenary"
        if 1 <= entropyten <= 5:
             encountermodifier = " Looking for a contract."
        if 6 <= entropyten <= 7:
             encountermodifier = " Asks the PCs if they've seen their target."
        if 8 <= entropyten <= 9:
             encountermodifier = " Following or is on the way to their target."
        if 10 <= entropyten <= 10:
             encountermodifier = " Mistakes a PC for their target."
    if zone == "SS":
        encounter = "Firefight (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Cops and robbers."
        if 4 <= entropyten <= 6:
             encountermodifier = " Cops and gangsters."
        if 7 <= entropyten <= 9:
             encountermodifier = " Drive-by shooting."
        if 10 <= entropyten <= 10:
             encountermodifier = " Gang War!"
    if zone == "TT":
        encounter = "Assassin"
        if 1 <= entropyten <= 7:
             encountermodifier = " Looks just like anybody else."
        if 8 <= entropyten <= 9:
             encountermodifier = " Looking for a contract."
        if 10 <= entropyten <= 10:
             encountermodifier = " In the middle of an op and has no qualms about terminating witnesses."
    if zone == "UU":
        encounter = "Skateboarders (1d4)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Recklessly skating through foot traffic."
        if 4 <= entropyten <= 6:
             encountermodifier = " Doing some cool tricks."
        if 7 <= entropyten <= 9:
             encountermodifier = " Doing some cool tricks off the PCs’ vehicle."
        if 10 <= entropyten <= 10:
             encountermodifier = " Fighting other skaters over something."
    if zone == "VV":
        encounter = "In-line Skaters (1d4)"
        if 1 <= entropyten <= 5:
             encountermodifier = " Recklessly skating through foot traffic."
        if 6 <= entropyten <= 7:
             encountermodifier = " Doing some tricks."
        if 8 <= entropyten <= 9:
             encountermodifier = " Doing some tricks off the PCs’ vehicle."
        if 10 <= entropyten <= 10:
             encountermodifier = " Skating through foot traffic and snagging personal belongings as they go."
    if zone == "WW":
        encounter = "Voodoo Priest"
        if 1 <= entropyten <= 6:
             encountermodifier = " Minding their own business."
        if 7 <= entropyten <= 8:
             encountermodifier = " Gathering Voodoo paraphernalia."
        if 9 <= entropyten <= 9:
             encountermodifier = " Arguing with somebody."
        if 10 <= entropyten <= 10:
             encountermodifier = " Places a curse on one of the PCs for some reason."
    if zone == "XX":
        encounter = "Stray Dog"
        if 1 <= entropyten <= 4:
             encountermodifier = " Running down the street."
        if 5 <= entropyten <= 6:
             encountermodifier = " Begging for some affection."
        if 7 <= entropyten <= 9:
             encountermodifier = " Begging for handouts."
        if 10 <= entropyten <= 10:
             encountermodifier = " Rabid and decides to attack the nearest living thing."
    if zone == "YY":
        encounter = "PediCab Driver"
        if 1 <= entropyten <= 4:
             encountermodifier = " Just hanging around."
        if 5 <= entropyten <= 7:
             encountermodifier = " Driving a fare."
        if 8 <= entropyten <= 10:
             encountermodifier = " Looking for a fare."
    if zone == "ZZ":
        encounter = "Psychopath"
        if 1 <= entropyten <= 3:
             encountermodifier = " Quietly mumbling to himself."
        if 4 <= entropyten <= 6:
             encountermodifier = " Screaming at the top of their lungs."
        if 7 <= entropyten <= 9:
             encountermodifier = " Asks the PCs about the voices in their head/aliens/small furry creatures/etc."
        if 10 <= entropyten <= 10:
             encountermodifier = " Has decided they have to get to the other side of a PC the hard way."
    if zone == "AAA":
        encounter = "Gamblers (1d4+1)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Playing a game of chance. Don't interrupt unless you got some creds."
        if 5 <= entropyten <= 7:
             encountermodifier = " Will ask the PCs to join them."
        if 8 <= entropyten <= 9:
             encountermodifier = " One player begs for some spare credits."
        if 10 <= entropyten <= 10:
             encountermodifier = " One loses severely, goes in to a fit of rage, and will attack the nearest person."
    if zone == "BBB":
        encounter = "Drunk"
        if 1 <= entropyten <= 4:
             encountermodifier = " Asks for some credits for a drink."
        if 5 <= entropyten <= 7:
             encountermodifier = " Passes out or is passed out in front of the PCs."
        if 8 <= entropyten <= 10:
             encountermodifier = " Offers the PCs a drink - don't insult him!"
    if zone == "CCC":
        encounter = "Drug Dealer"
        if 1 <= entropyten <= 6:
             encountermodifier = " Tries to sell the PCs some goods. 'The first time's free!'"
        if 7 <= entropyten <= 8:
             encountermodifier = " High himself."
        if 9 <= entropyten <= 10:
             encountermodifier = " Running from the police. A firefight may ensue."
    if zone == "DDD":
        encounter = "Black Security (1d4+2)"
        if 1 <= entropyten <= 5:
             encountermodifier = " On break."
        if 6 <= entropyten <= 10:
             encountermodifier = " Busy shooting the mess out of someone or something."
    if zone == "EEE":
        encounter = "Yello Bike"
        if 1 <= entropyten <= 4:
             encountermodifier = " Just been picked up by someone."
        if 5 <= entropyten <= 8:
             encountermodifier = " Free for the taking. Just be sure to leave it for someone else when you are through with it."
        if 9 <= entropyten <= 10:
             encountermodifier = " Being vandalized by a couple of kids."
    if zone == "FFF":
        encounter = "TechnoMage"
        if 1 <= entropyten <= 7:
             encountermodifier = " Minding their own business and looks just like anybody else."
        if 8 <= entropyten <= 8:
             encountermodifier = " Doing some tricks for some stray kids."
        if 9 <= entropyten <= 9:
             encountermodifier = " Teaching somebody a lesson - without anybody knowing."
        if 10 <= entropyten <= 10:
             encountermodifier = " Decides the PCs don't respect technology and will set them straight - unbeknownst to them, of course."
    if zone == "GGG":
        encounter = "Merchant"
        if 1 <= entropyten <= 6:
             encountermodifier = " Hawking goods."
        if 7 <= entropyten <= 8:
             encountermodifier = " Will try to buy a trinket off of a PC."
        if 9 <= entropyten <= 10:
             encountermodifier = " Accuses a PC of shoplifting and will call the police."
    if zone == "HHH":
        encounter = "Shaman"
        if 1 <= entropyten <= 5:
             encountermodifier = " Just minding their own business."
        if 6 <= entropyten <= 9:
             encountermodifier = " Collecting items for their medicine bag."
        if 10 <= entropyten <= 10:
             encountermodifier = " Performing a ritual in the middle of an alley."
    if zone == "III":
        encounter = "Street Peddler"
        if 1 <= entropyten <= 6:
             encountermodifier = " Pesters the PCs to buy something."
        if 7 <= entropyten <= 8:
             encountermodifier = " Will try to buy a trinket off of a PC."
        if 9 <= entropyten <= 10:
             encountermodifier = " Accuses a PC of shoplifting and will call the police."
    if zone == "JJJ":
        encounter = "Police (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Stopped for a snack."
        if 4 <= entropyten <= 6:
             encountermodifier = " Are asking questions about a suspect."
        if 7 <= entropyten <= 9:
             encountermodifier = " Ask to see some papers on, “all that hardware you got!”"
        if 10 <= entropyten <= 10:
             encountermodifier = " Are apprehending a suspect."
    if zone == "KKK":
        encounter = "Drug Raid (1d4+2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Cops have the place staked out."
        if 5 <= entropyten <= 7:
             encountermodifier = " Cops are on their way in."
        if 8 <= entropyten <= 10:
             encountermodifier = " Panic fire randomly sprays the street."
    if zone == "LLL":
        encounter = "Mutant"
        if 1 <= entropyten <= 4:
             encountermodifier = " Minding their own business."
        if 5 <= entropyten <= 7:
             encountermodifier = " Asking for money to fund research into the medical technology to reverse their ailments (or bring down the company responsible)."
        if 8 <= entropyten <= 9:
             encountermodifier = " Trying to hide from the group of people pointing and snickering."
        if 10 <= entropyten <= 10:
             encountermodifier = " Will beat the snot out of the PCs if they even look at him."
    if zone == "MMM":
        encounter = "Street Doc"
        if 1 <= entropyten <= 4:
             encountermodifier = " Generally wandering around looking for a quick job"
        if 5 <= entropyten <= 7:
             encountermodifier = " Patching up some victim."
        if 8 <= entropyten <= 10:
             encountermodifier = " Offers the PCs some used body parts or cyberware."
    if zone == "NNN":
        encounter = "Fixer"
        if 1 <= entropyten <= 3:
             encountermodifier = " Offers their business card."
        if 4 <= entropyten <= 6:
             encountermodifier = " Tries to pawn off goods."
        if 7 <= entropyten <= 10:
             encountermodifier = " Conducting business - don't bother him!"
    if zone == "OOO":
        encounter = "Prostitutes (1d4)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Flagging down a John."
        if 4 <= entropyten <= 6:
             encountermodifier = " Offer their services."
        if 7 <= entropyten <= 8:
             encountermodifier = " Ask the PCs to hide them from the law."
        if 9 <= entropyten <= 10:
             encountermodifier = " Running from their pimp and ask for help."
    if zone == "PPP":
        encounter = "Beggar"
        if 1 <= entropyten <= 5:
             encountermodifier = " Asks for some spare credits."
        if 6 <= entropyten <= 8:
             encountermodifier = " Demands for some spare credits and will get violent if refused."
        if 9 <= entropyten <= 10:
             encountermodifier = " Being beaten by some street punks."
    if zone == "QQQ":
        encounter = "Bum"
        if 1 <= entropyten <= 4:
             encountermodifier = " Sleeping on the sidewalk in front of the PCs."
        if 5 <= entropyten <= 7:
             encountermodifier = " Asks for some spare credits."
        if 8 <= entropyten <= 10:
             encountermodifier = " Talks to himself - if the PCs interrupt him, he'll get louder and get crazy."
    if zone == "RRR":
        encounter = "Nomads (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Just passing through town."
        if 4 <= entropyten <= 5:
             encountermodifier = " Stocking up on supplies."
        if 6 <= entropyten <= 7:
             encountermodifier = " Heading for the local tavern."
        if 8 <= entropyten <= 9:
             encountermodifier = " Looking for someone who done them wrong."
        if 10 <= entropyten <= 10:
             encountermodifier = " Decide to rough the PCs up a bit - just because they're funny lookin'."
    if zone == "SSS":
        encounter = "Pickpocket"
        if 1 <= entropyten <= 3:
             encountermodifier = " Tries to pawn off some 'new' goods."
        if 4 <= entropyten <= 6:
             encountermodifier = " Running from the law."
        if 7 <= entropyten <= 10:
             encountermodifier = " Tries to pickpocket a PC as they pass."
    if zone == "TTT":
        encounter = "Thief"
        if 1 <= entropyten <= 4:
             encountermodifier = " Tries to pawn off some 'new' goods."
        if 5 <= entropyten <= 7:
             encountermodifier = " Running from the law."
        if 8 <= entropyten <= 10:
             encountermodifier = " Tries to rob the PCs at gunpoint."
    if zone == "UUU":
        encounter = "Rats"
        if 1 <= entropyten <= 5:
             encountermodifier = " Scurrying down an alley."
        if 6 <= entropyten <= 9:
             encountermodifier = " Devouring some animal carcass or bit of trash."
        if 10 <= entropyten <= 10:
             encountermodifier = " Rabid and decide to attack the nearest living thing."
    if zone == "VVV":
        encounter = "BloodGang (generic anti-cyberware gang) (1d4+2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Just prowling around."
        if 5 <= entropyten <= 7:
             encountermodifier = " Decide to lean on a couple of civilians."
        if 8 <= entropyten <= 9:
             encountermodifier = " Decide to lean on a PC for owning cyberware."
        if 10 <= entropyten <= 10:
             encountermodifier = " Gang War! Bloods -vs- Chromers. And the PCs are caught in the middle."
    if zone == "WWW":
        encounter = "SteelGang (generic ARMED street gang) (1d4+2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Just prowling around."
        if 5 <= entropyten <= 7:
             encountermodifier = " Decide to lean on a couple of civilians."
        if 8 <= entropyten <= 9:
             encountermodifier = " Decide to lean on the PCs."
        if 10 <= entropyten <= 10:
             encountermodifier = " Gang War! Steels -vs- Bloods. And the PCs are caught in the middle."
    if zone == "XXX":
        encounter = "PoserGang (generic poser or corpkid gang) (1d4+2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Just showing off their trendy outfits."
        if 5 <= entropyten <= 7:
             encountermodifier = " Decide to tease a couple of civilians."
        if 8 <= entropyten <= 9:
             encountermodifier = " Will beat the snot out of the PCs if they make any comment."
        if 10 <= entropyten <= 10:
             encountermodifier = " Fashion Feud! And the PCs are caught in the middle without their cashmere."
    if zone == "YYY":
        encounter = "Chromers (generic cyber-enhanced gang) (1d4+2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Just prowling around."
        if 5 <= entropyten <= 7:
             encountermodifier = " Decide to lean on a couple of civilians."
        if 8 <= entropyten <= 9:
             encountermodifier = " Decide to lean on the PCs."
        if 10 <= entropyten <= 10:
             encountermodifier = " Gang War! Chromers -vs- Anybody. And the PCs are caught in the middle."
    if zone == "ZZZ":
        encounter = "Biker Gang (1d4+1)"
        if 1 <= entropyten <= 3:
             encountermodifier = " Riding around looking for some trouble."
        if 4 <= entropyten <= 6:
             encountermodifier = " Stopped for a quick snack. Don't touch... don't look at... don't even think about their bikes!"
        if 7 <= entropyten <= 9:
             encountermodifier = " Decide to play chicken with pedestrians."
        if 10 <= entropyten <= 10:
             encountermodifier = " Dragging somebody down the street with a chain."
    if zone == "AAAA":
        encounter = "Body Baggers (2)"
        if 1 <= entropyten <= 4:
             encountermodifier = " Are dragging a body bag down the street."
        if 5 <= entropyten <= 7:
             encountermodifier = " Are scoping the area for new vict... er, bodies."
        if 8 <= entropyten <= 9:
             encountermodifier = " Ask to tag along with the PCs."
        if 10 <= entropyten <= 10:
             encountermodifier = " If the PCs look weak enough, they will attack them."

    return (encounter,encountermodifier)
main()
