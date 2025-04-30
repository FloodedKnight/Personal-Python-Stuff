# For the game "Friday Night Funkin". Reads chart data, and puts it into a string. Here is the format of the string
# noteColor_waitTime_noteColor
# So if it was red_20_green, it would spawn a red arrow, wait 20 ticks (1 second), and then spawn a green note.
# Also supports hold notes: red*100_20_green means the same thing as before, except the red note should be held be held down for 100 units (i havent checked what this unit is yet, im just reading it off the chart data. its probably like 0.01s)

import json

def convertFNFtoSkript(chart):
    player1_notes = []
    player2_notes = []

    for section in chart["song"]["notes"]:
        for note in section["sectionNotes"]:
            time = note[0] 
            arrow = note[1]
            if len(note) > 2:
                if type(note[2]) == int:
                    sustain = note[2]
                else:
                    sustain = 0
            else:
                sustain = 0
            if section["mustHitSection"] == True:
                player1_notes.append((time, arrow, sustain))
            else:
                player2_notes.append((time, arrow, sustain))

    
    player1_notes.sort() 
    player2_notes.sort()

    arrowLink = {0: "red", 
                 1: "green", 
                 2: "blue", 
                 3: "pink"}
    
    output = []
    lastTime = 0
    
    for time, arrow, sustain in player1_notes:
        waitTime = round((time - lastTime) / (1000 / 20))  # Convert to Minecraft Ticks
        if waitTime > 0:
            output.append(str(waitTime))
        if arrow in arrowLink:
            addArr = arrowLink[arrow]
            if sustain > 0:
                addArr += "*" + str(sustain)
            output.append(addArr)
        lastTime = time

    output2 = []
    lastTime = 0
    for time, arrow, sustain in player2_notes:
        waitTime = round((time - lastTime) / (1000 / 20))  # Convert to Minecraft Ticks
        if waitTime > 0:
            output2.append(str(waitTime))
        if arrow in arrowLink:
            addArr = arrowLink[arrow]
            if sustain > 0:
                addArr += "*" + str(sustain)
            output2.append(addArr)
        lastTime = time


    #& FOR MUSIC-CHART SYNCING STUFF
    # for i in range(len(output)):
    #     if type(output[i]) == int:
    #         if i > 200 and output[i] > 20:
    #             output[i] += random.choice([5, 6])
    #         output[i] = str(output[i])

    # for i in range(len(output2)):
        #     if type(output[i]) == int:
        #         if i > 200 and output2[i] > 20:
        #             output2[i] += random.choice([5, 6])
        #         output2[i] = str(output2[i])
    
    return "_".join(output), "_".join(output2)

with open("yourJSON", "r") as file:
    fnf_chart = json.load(file)

converted_chart = convertFNFtoSkript(fnf_chart)
print("OPPONENT NOTES: \n\n\n" + converted_chart[1])

print("\n\n\nPLAYER1 NOTES:\n\n\n" + converted_chart[0])
