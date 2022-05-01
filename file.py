#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

G = pd.read_csv("logs.csv", low_memory=False)

colsToKeep = ["player_id", "school", "date", "event_id", 
"event_time_dbl", "stack_title", "avatar_gender", "proportion_complete",
"avatar_id"]

H = G.drop(G.columns.difference(colsToKeep), 1)
#print(H.head())

#players = [y for x, y in G.groupby("player_id", as_index=False)]


# player 6607011 data
#player = H.loc[H["player_id"] == 6607011]
#print(player.head())
#print("max completion: ", player["proportion_complete"].max())


schools = H["school"].unique()

schoolDict = {3561 : [], 2570 : [], 1827 : [], 647 : [],
              2238 : [], 5340 : [], 4829 : [], 1531 : [],
              9691 : [], 7167 : [], 6266 : [], 3205 : []}

raceDict = {"African American" : [], "Hispanic" : [], "Caucasian" : []}

completion_arr = []
maleScores = []
femaleScores = []



for id in H["player_id"].unique():
    player = H.loc[H["player_id"] == id]

    # get player's completion
    completion = player["proportion_complete"].max()
    
    # get player (avatar) gender
    row =  player.loc[player["event_id"] == 602]
    if(row.iloc[0]["avatar_gender"] == "Male"):
        maleScores.append(completion)
    else:
        femaleScores.append(completion)
    
    s = player["school"].values[0]
    schoolDict.get(s).append(completion)
    if(s == 6266):
        

    xd = player.loc[player["event_id"] == 604].iloc[0]["avatar_id"]
    raceDict.get(xd).append(completion)
    completion_arr.append(completion)



averages = []
for item in schoolDict.values():
    averages.append(np.average(item))

raceAvg = []
for item in raceDict.values():
    raceAvg.append(np.average(item))


fig, (ax1, ax2, ax3) = plt.subplots(3)
p1 = ax1.bar(np.arange(12), averages, width=0.35)
ax1.set_ylabel("Average Completion")
ax1.set_xlabel("Schools")
ax1.set_xticks(np.arange(12))
ax1.set_xticklabels(schools)

p2 = ax2.hist(completion_arr, bins=[0, 0.08, 0.16, 0.24, 0.32, 0.4, 0.48, 
                                        0.56, 0.64, 0.72, 0.8, 0.88, 1])
ax2.set_ylabel("Frequency")
ax2.set_xlabel("Completion")

#p3 = ax3.bar([0,1], [np.average(maleScores), np.average(femaleScores)])
#ax3.set_ylabel("Average Completion")
#ax3.set_xlabel("Gender")
#ax3.set_xticks([0,1])
#ax3.set_xticklabels(["Male", "Female"])
#ax3.set_ylim([0,1])
print("Male avg: ", np.average(maleScores), "Female avg: ", np.average(femaleScores))

p3 = ax3.bar([0,1,2], raceAvg)
ax3.set_ylabel("Average Completion")
ax3.set_xlabel("Ethnicity")
ax3.set_xticks([0,1,2])
ax3.set_xticklabels(["African American", "Hispanic", "Caucasian"])
ax3.set_ylim([0,1])


plt.show()