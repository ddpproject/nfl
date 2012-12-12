import pymongo
import utils
from collections import defaultdict

def sortQBs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedQB = db['QB']
    rankedQB.drop()

    for each in player_collection.find( {"Position" : 'QB'} ):
        if "Passing" in each:
            passingTD = int(each['Passing']['TD'])
            passingYds = int(str(each['Passing']['Yds']).replace(",", ""))
            passingComp = int(each['Passing']['Comp'])
            passingPct = 10 * float(each['Passing']['Pct'])
            passingInt = int(each['Passing']['Int'])
            passingSck = int(each['Passing']['Sck'])
            passingTotal = (passingTD * 200) + (passingYds * 2) + (passingComp * 10) + (10 * (passingPct - 50) ) - (passingInt * 200) - (passingSck * 25)
        else:
            passingTotal = 0
        if "Rushing" in each:
            rushingTD = each['Rushing']['TD']
            rushingFUM = each['Rushing']['FUM']
            rushingYds = each['Rushing']['Yds']
            rushingTotal = (rushingTD * 150) + (rushingYds * 2) - (rushingFUM * 150)
        else:
            rushingTotal = 0
        totalScore = passingTotal + rushingTotal
        each['Score'] = totalScore
        rankedQB.insert(each)

    for each in rankedQB.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortRBs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedRB = db['RB']
    rankedRB.drop()

    for each in player_collection.find( {"Position" : 'RB'} ):
        if "Rushing" in each:
            rushingTD = each['Rushing']['TD']
            rushingFUM = each['Rushing']['FUM']
            rushingYds = each['Rushing']['Yds']
            rushingTotal = (rushingTD * 700) + (rushingYds * 8) - (rushingFUM * 500)
        else:
            rushingTotal = 0
        if "Receiving" in each:
            receivingTD = int(each['Receiving']['TD'])
            receivingYds = int(str(each['Receiving']['Yds']).replace(",", ""))
            receivingFum = int(each['Receiving']['FUM'])
            receptions = int(each['Receiving']['Rec'])
            receivingTotal = (receivingTD * 650) + (receivingYds * 6) - (receivingFum * 300) + (receptions * 75 )
        else:
            receivingTotal = 0
        if "Kick Return" in each:
            kreturnTD = int(each['Kick Return']['TD'])
            kreturnYds = int(str(each['Kick Return']['Yds']).replace(",", ""))
            kreturnFum = int(each['Kick Return']['FUM'])
            kreturnTotal = (kreturnTD * 600) + (kreturnYds * 1) - (kreturnFum * 350)
        else:
            kreturnTotal = 0
        if "Punt Return" in each:
            preturnTD = int(each['Punt Return']['TD'])
            preturnYds = int(str(each['Punt Return']['RetY']).replace(",", ""))
            preturnFum = int(each['Punt Return']['FUM'])
            preturnTotal = (preturnTD * 600) + (preturnYds * 2) - (preturnFum * 350)
        else:
            preturnTotal = 0
        totalScore = rushingTotal + receivingTotal + kreturnTotal + preturnTotal
        each['Score'] = totalScore
        rankedRB.insert(each)
  
    for each in rankedRB.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortTEs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedTE = db['TE']
    rankedTE.drop()

    for each in player_collection.find( {"Position" : 'TE'} ):
        if "Receiving" in each:
            receivingTD = int(each['Receiving']['TD'])
            receivingYds = int(str(each['Receiving']['Yds']).replace(",", ""))
            receivingFum = int(each['Receiving']['FUM'])
            receptions = int(each['Receiving']['Rec'])
            receivingTotal = (receivingTD * 600) + (receivingYds * 8) - (receivingFum * 300) + (receptions * 100 )
        else:
            receivingTotal = 0
        totalScore = receivingTotal
        each['Score'] = totalScore
        rankedTE.insert(each)
  
    for each in rankedTE.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortWRs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedWR = db['WR']
    rankedWR.drop()

    for each in player_collection.find( {"Position" : 'WR'} ):
        if "Receiving" in each:
            receivingTD = int(each['Receiving']['TD'])
            receivingYds = int(str(each['Receiving']['Yds']).replace(",", ""))
            receivingFum = int(each['Receiving']['FUM'])
            receptions = int(each['Receiving']['Rec'])
            receivingTotal = (receivingTD * 600) + (receivingYds * 8) - (receivingFum * 250) + (receptions * 100 )
        else:
            receivingTotal = 0
        if "Kick Return" in each:
            kreturnTD = int(each['Kick Return']['TD'])
            kreturnYds = int(str(each['Kick Return']['Yds']).replace(",", ""))
            kreturnFum = int(each['Kick Return']['FUM'])
            kreturnTotal = (kreturnTD * 600) + (kreturnYds * 1) - (kreturnFum * 350)
        else:
            kreturnTotal = 0
        if "Punt Return" in each:
            preturnTD = int(each['Punt Return']['TD'])
            preturnYds = int(str(each['Punt Return']['RetY']).replace(",", ""))
            preturnFum = int(each['Punt Return']['FUM'])
            preturnTotal = (preturnTD * 600) + (preturnYds * 2) - (preturnFum * 350)
        else:
            preturnTotal = 0
        print each
        totalScore = receivingTotal + kreturnTotal + preturnTotal
        each['Score'] = totalScore
        rankedWR.insert(each)
  
    for each in rankedWR.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortDBs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedDB = db['DB']
    rankedDB.drop()

    for each in player_collection.find({ "$or" : [ {"Position" : 'FS'} , {"Position" : 'SS'} , {"Position" : 'CB'} , {"Position" : 'DB'} , {"Position" : 'SAF'} ] } ):
        if "Defensive" in each:
            defenseSolo = int(each['Defensive']['Total'])
            defenseAst = int(each['Defensive']['Ast'])
            defenseSack = int(each['Defensive']['Sck'])
            defensePDef = int(each['Defensive']['PDef'])
            defenseInt = int(each['Defensive']['Int'])
            defenseTD = int(each['Defensive']['TDs'])
            defenseYds = int(each['Defensive']['Yds'])
            defenseTotal = (defenseSolo * 100) + (defenseAst * 50) + (defenseSack * 200) + (defensePDef * 200) + (defenseInt * 500) + (defenseTD * 200) + (defenseYds * 5)
        else:
            defenseTotal = 0
        if "Fumbles" in each:
            ForcedFumble = int(each['Fumbles']['FF'])
            FumbleTD = int(each['Fumbles']['TD'])
            fumbleTotal = (ForcedFumble * 500) + (FumbleTD * 200)
        else:
            fumbleTotal = 0
        if "Kick Return" in each:
            kreturnTD = int(each['Kick Return']['TD'])
            kreturnYds = int(str(each['Kick Return']['Yds']).replace(",", ""))
            kreturnFum = int(each['Kick Return']['FUM'])
            kreturnTotal = (kreturnTD * 600) + (kreturnYds * 1) - (kreturnFum * 350)
        else:
            kreturnTotal = 0
        if "Punt Return" in each:
            preturnTD = int(each['Punt Return']['TD'])
            preturnYds = int(str(each['Punt Return']['RetY']).replace(",", ""))
            preturnFum = int(each['Punt Return']['FUM'])
            preturnTotal = (preturnTD * 600) + (preturnYds * 2) - (preturnFum * 350)
        else:
            preturnTotal = 0
        totalScore = defenseTotal + kreturnTotal + preturnTotal + fumbleTotal
        each['Score'] = totalScore
        rankedDB.insert(each)
  
    for each in rankedDB.find().sort('Score',-1):
        print each['Name']
        print each['Score']


def sortLBs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedLB = db['LB']
    rankedLB.drop()

    for each in player_collection.find({ "$or" : [ {"Position" : 'LB'} , {"Position" : 'OLB'} , {"Position" : 'MLB'} , {"Position" : 'ILB'}]}):
        if "Defensive" in each:
            defenseSolo = int(each['Defensive']['Total'])
            defenseAst = int(each['Defensive']['Ast'])
            defenseSack = int(each['Defensive']['Sck'])
            defensePDef = int(each['Defensive']['PDef'])
            defenseInt = int(each['Defensive']['Int'])
            defenseTD = int(each['Defensive']['TDs'])
            defenseYds = int(each['Defensive']['Yds'])
            defenseTotal = (defenseSolo * 100) + (defenseAst * 50) + (defenseSack * 350) + (defensePDef * 150) + (defenseInt * 500) + (defenseTD * 500) + (defenseYds * 5)
        else:
            defenseTotal = 0
        if "Fumbles" in each:
            ForcedFumble = int(each['Fumbles']['FF'])
            FumbleTD = int(each['Fumbles']['TD'])
            fumbleTotal = (ForcedFumble * 500) + (FumbleTD * 500)
        else:
            fumbleTotal = 0
        totalScore = defenseTotal + fumbleTotal
        each['Score'] = totalScore
        rankedLB.insert(each)
    
    for each in rankedLB.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortDLs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedDL = db['DL']
    rankedDL.drop()

    for each in player_collection.find({ "$or" : [ {"Position" : 'NT'} , {"Position" : 'DT'} , {"Position" : 'DE'}]}):
        if "Defensive" in each:
            defenseSolo = int(each['Defensive']['Total'])
            defenseAst = int(each['Defensive']['Ast'])
            defenseSack = int(each['Defensive']['Sck'])
            defensePDef = int(each['Defensive']['PDef'])
            defenseInt = int(each['Defensive']['Int'])
            defenseTD = int(each['Defensive']['TDs'])
            defenseYds = int(each['Defensive']['Yds'])
            defenseTotal = (defenseSolo * 100) + (defenseAst * 50) + (defenseSack * 350) + (defensePDef * 150) + (defenseInt * 500) + (defenseTD * 500) + (defenseYds * 5)
        else:
            defenseTotal = 0
        if "Fumbles" in each:
            ForcedFumble = int(each['Fumbles']['FF'])
            FumbleTD = int(each['Fumbles']['TD'])
            fumbleTotal = (ForcedFumble * 500) + (FumbleTD * 500)
        else:
            fumbleTotal = 0
        totalScore = defenseTotal + fumbleTotal
        each['Score'] = totalScore
        rankedDL.insert(each)
    
    for each in rankedDL.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortKs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedK = db['K']
    rankedK.drop()

    for each in player_collection.find( {"Position" : 'K'} ):
        if "Field Goal Kickers" in each:
            extraPointAttempt = int(each['Field Goal Kickers']['XP Att'])
            extraPointMade = int(each['Field Goal Kickers']['XPM'])
            fgAttempt = int(each['Field Goal Kickers']['FG Att'])
            fgMade = int(each['Field Goal Kickers']['FGM'])
            kickingTotal = (float(extraPointMade)*1000/(extraPointAttempt))+ (float(fgMade)*1000/(fgAttempt))
        else:
            kickingTotal = 0
        
        each['Score'] = kickingTotal
        rankedK.insert(each)

    for each in rankedK.find().sort('Score',-1):
        print each['Name']
        print each['Score']

def sortPs():
    db = utils.connect_db('nfl', remove_existing = False)
    player_collection = db['players']
    
    rankedP = db['P']
    rankedP.drop()

    for each in player_collection.find( {"Position" : 'P'} ):
        if "Punting Stats" in each:
            netAvg = float(each['Punting Stats']['Net Avg'])
            puntingAvg = float(each['Punting Stats']['Avg'])
            inside20 = int(each['Punting Stats']['IN 20'])
            puntingTotal = (netAvg * 10) + (puntingAvg * 10) + (inside20 * 10)
        else:
            puntingTotal = 0
        
        each['Score'] = puntingTotal
        rankedP.insert(each)

    for each in rankedP.find().sort('Score',-1):
        print each['Name']
        print each['Score']

if __name__=="__main__":
    sortQBs()
    sortRBs()
    sortTEs()
    sortWRs()
    sortDBs()
    sortLBs()
    sortDLs()
    sortKs()
    sortPs()
