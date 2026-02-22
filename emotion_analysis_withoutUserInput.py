
with open("Scripts/scene_info.txt",'r') as f: 
    f_scene=f.read()

    scene_list= f_scene.strip().split("\n")
#Scene list = reading the document and stripping it, splitting it at every line
   

    table=[]
    #Empty Table
    total_scene_length=0
    #Setting new variable scene length to 0


    for line in scene_list:
        line=line.strip()
        parts = line.split(", ")
        shot=int(parts[0])
        emotion = parts[1]
        length= float(parts[2])
        table.append([shot,emotion,length])
        #for every line in the scene list, it strips the empty space on the sides
        #Then "parts" is the line split by a comma. Everytime there is a , it creates a new part of "parts" - you get 3 parts per scene 
        #Then shot = the integer version of the 1st part of "parts"
        #Emotion = the 2nd part of "parts"
        #Length = the 3rd part of "parts"
        #Append adds it to the end of table. Now each row in tablne is made up of the shot, emotion, length. These values keep changing everytime in the loop

    unique_emotions=[]
    for row in table: 
        emotion = row[1]
        if emotion not in unique_emotions:
            unique_emotions.append(emotion)
    #Creates a new table called unique emotions
    #For every row in the table created in the previous loop, emotion is equal to the 2nd part of the row 
    #If the emotion (that the loop is looking at) isn't in unique emotions, add it
    
    for emotion in unique_emotions:
        total_length=0
        count=0
        for row in table: 
            if row[1] == emotion: 
                total_length += (row[2])
                count +=1
        average = total_length/count
        print(emotion, "average length:", round(average,2))
    
    #Then it loops through this list of unique emotions
    #Creates variables total length and count and sets them to 0 initially
    #Then it again goes through every row in the original table, checking to see if the second part of the row (emotions) matches the emotions in the higher loop 
    #If it matches, then you add the third part of the row (aka the scene length) to the total length and increase the count by 1
    #Finally the two values are divided to get the average length 
    #This value is printed - and then the loop goes to the next unique emotion, looping through the whole table again. The values of total length/count keep changing
    ##
    new_table=[]
    most_common_emotion= ""
    highest_count=0
    highest_plural=[]
    for emotion in unique_emotions:
        emotion_count=0
        for row in table:
            if row[1]== emotion:
                emotion_count+=1
        
        if (emotion_count>highest_count):
            highest_count=emotion_count
            most_common_emotion=emotion
            highest_plural.append(emotion)
        elif ((emotion_count==highest_count) and (emotion not in highest_plural)):
            highest_plural.append(emotion)
            
    print(highest_plural)
    print("These emotions are the most common and appeared in "+str(highest_count)+" scenes each.")
    ##
    #now i want to create one that sees which emotion occupies the most length of time 
    longest_emotion=""
    length_of_longest_emotion=0
    for emotion in unique_emotions:
        length_of_emotion=0
        for row in table:
            if row[1]==emotion:
                length_of_emotion=length_of_emotion+row[2]
       
        if length_of_emotion > length_of_longest_emotion:
            length_of_longest_emotion=length_of_emotion
            longest_emotion=emotion
    print("The emotion which takes up the majority of the film is " + longest_emotion + " and it occupies " + str(length_of_longest_emotion)+ " seconds.")
    ##
    for row in table: 
        total_scene_length +=row[2]
    
    #For every row in the table, the third value aka [2] is added to the total_scene_length
    
    overall_average = total_scene_length/len(table)
    print("Overall average scene length:", round(overall_average,1))
    #Calculates the overall average by divided the total scenes lengths by the length of the table (aka the number of scenes)
    #Prints the overall scene length rounded to 1 decimal place
    
    
#print(table)
#Prints the table duh 
   


    
#Emotion which takes up the longest length of time
# Most common emotion in terms of number of scenes 