#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:16:44 2021

@author: niczacharis
"""

import pandas as pd
import numpy as np

shotsData = pd.read_csv("shots_data.csv")

## Get shot zones for both teams
# corner three -> x coordinate > 22 or < -22 and y coordinate <= 7.8
cornerThreeData = shotsData[(shotsData['x'] > 22.0) & (shotsData['y'] <= 7.8) | 
                                 (shotsData['x'] < -22.0) & (shotsData['y'] <= 7.8)]

# non corner three -> (x^2 + y^2)^.5 > 23.75 and y coordinate > 7.8
nonCornerThreeData = shotsData[(((shotsData['y'] ** 2) + (shotsData['x'] ** 2)) ** 0.5 > 23.75) 
                               & (shotsData['y'] > 7.8)]

# create a list of the indices with three point attempts
threePointList = cornerThreeData.index.to_list()
threePointList = threePointList + nonCornerThreeData.index.to_list()

# 2 pt attempts are all indices not in the three point list
twoPointData = shotsData.loc[~shotsData.index.isin(threePointList)]


## Divide data up by team
shotsA = shotsData.loc[shotsData['team'] == 'Team A']
shotsB = shotsData.loc[shotsData['team'] == 'Team B']

cornerA = cornerThreeData.loc[cornerThreeData['team'] == 'Team A']
cornerB = cornerThreeData.loc[cornerThreeData['team'] == 'Team B']

nonCornerA = nonCornerThreeData.loc[nonCornerThreeData['team'] == 'Team A']
nonCornerB = nonCornerThreeData.loc[nonCornerThreeData['team'] == 'Team B']

twoA = twoPointData.loc[twoPointData['team'] == 'Team A']
twoB = twoPointData.loc[twoPointData['team'] == 'Team B']


## Determine Shot distribution in each zone
cornerDistributionA = (len(cornerA) / len(shotsA)) * 100
nonCornerDistributionA = (len(nonCornerA) / len(shotsA)) * 100
twoPointDistributionA = (len(twoA) / len(shotsA)) * 100

cornerDistributionB = (len(cornerB) / len(shotsB)) * 100
nonCornerDistributionB = (len(nonCornerB) / len(shotsB)) * 100
twoPointDistributionB = (len(twoB) / len(shotsB)) * 100


## Determine eFG% in each zone
cornerEFGA = ((len(cornerA.loc[cornerA['fgmade'] == 1]) + (0.5 * (len(cornerA.loc[cornerA['fgmade'] == 1])))) / len(cornerA)) * 100
nonCornerEFGA = ((len(nonCornerA.loc[nonCornerA['fgmade'] == 1]) + (0.5 * (len(nonCornerA.loc[nonCornerA['fgmade'] == 1])))) / len(nonCornerA)) * 100
twoPointEFGA = ((len(twoA.loc[twoA['fgmade'] == 1])) / len(twoA)) * 100

cornerEFGB = ((len(cornerB.loc[cornerB['fgmade'] == 1]) + (0.5 * (len(cornerB.loc[cornerB['fgmade'] == 1])))) / len(cornerB)) * 100
nonCornerEFGB = ((len(nonCornerB.loc[nonCornerB['fgmade'] == 1]) + (0.5 * (len(nonCornerB.loc[nonCornerB['fgmade'] == 1])))) / len(nonCornerB)) * 100
twoPointEFGB = ((len(twoB.loc[twoB['fgmade'] == 1])) / len(twoB)) * 100

print('EFG %\n\n'
      + 'C3A: ' + str(cornerEFGA) +'%\n'
      + 'NC3A: ' + str(nonCornerEFGA) +'%\n'
      + '2PTA: ' + str(twoPointEFGA) +'%\n'
      + 'C3B: ' + str(cornerEFGB) +'%\n'
      + 'NC3B: ' + str(nonCornerEFGB) +'%\n'
      + '2PTB: ' + str(twoPointEFGB) +'%\n')

print('Distribution %\n\n'
      + 'C3A: ' + str(cornerDistributionA) +'%\n'
      + 'NC3A: ' + str(nonCornerDistributionA) +'%\n'
      + '2PTA: ' + str(twoPointDistributionA) +'%\n'
      + 'C3B: ' + str(cornerDistributionB) +'%\n'
      + 'NC3B: ' + str(nonCornerDistributionB) +'%\n'
      + '2PTB: ' + str(twoPointDistributionB) +'%\n')








