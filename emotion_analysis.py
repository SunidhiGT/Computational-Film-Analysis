
with open("Scripts/scene_info.txt",'r') as f: 
    f_scene=f.read()

    scene_list= f_scene.strip().split("\n")
 
    table=[]
    total_scene_length=0
    unique_emotions=[]

    for line in scene_list:
        line=line.strip()
        parts = line.split(", ")
        shot=int(parts[0])
        emotion = parts[1]
        length= float(parts[2])
        table.append([shot,emotion,length])
    
    for row in table: 
                emotion = row[1]
                if emotion not in unique_emotions:
                    unique_emotions.append(emotion)

    user_choice=input("1.See average scene length per emotion\n2.See the most common emotion\n3.See emotion occupying the most time\n4.See overall average pacing\n5.Information by emotion\nEnter a number here: ")
    user_choice=int(user_choice)
    if user_choice==1:
        for emotion in unique_emotions:
            total_length=0
            count=0
            for row in table: 
                if row[1] == emotion: 
                    total_length += (row[2])
                    count +=1
            average = total_length/count
            print(emotion, "average length:", round(average,2))
    if user_choice==2:
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
    if user_choice==3:
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
    if user_choice==4:
        for row in table: 
            total_scene_length +=row[2]
            overall_average = total_scene_length/len(table)
        print("Overall average scene length: "+ str(round(overall_average,1))+" seconds.") 

        if overall_average<2:
            print("There is rapid pacing, about 30+ cuts/min, and the editing may feel chaotic and fragmented. This editing style is common in action movies, thrillers, and fight scenes.")
        elif 2<=overall_average<=3:
            print("There is fast pacing, about 15-30 cuts/min, and the editing may feel energetic yet intense. This editing style is common in horror movies, trailers, and action movies. ")
        elif 3<overall_average<=6:
            print("There is moderately fast pacing, about 6-10 cuts/min, and the editing may feel dynamic. This editing style is common in dramas and tension filled conversations.")
        elif 6<overall_average<=10:
            print("There is moderate pacing, about 6-10 cuts/min, and the editing may feel balanced. This editing style is common in most mainstream films")
        elif 10<overall_average<=20:
            print("There is slow pacing, about 3-6 cuts/min, and the editing may feel observational. This editing style is common in Indie dramas and romance films.")
        elif overall_average>20:
            print("There is very slow pacing, about less than 3 cuts per minute, and the editing may feel immersive or uninterrupted. This editing style is common in art cinema and Tarkovsky-style films")
    if user_choice==5:
        user_picks_emotion=input("Enter an Emotion: ")
        length_of_emotion=0
        number_of_scenes_with_the_emotion=0
        if user_picks_emotion in unique_emotions:
            for row in table:
                if row[1]==user_picks_emotion:
                    length_of_emotion=length_of_emotion+row[2]
                    number_of_scenes_with_the_emotion+=1
            average_length_of_selected_emotion=length_of_emotion/number_of_scenes_with_the_emotion
            average_length_of_selected_emotion=round(average_length_of_selected_emotion,2)
            print(user_picks_emotion+ " has "+ str(length_of_emotion)+" seconds of screentime, an average length of "+str(average_length_of_selected_emotion)+" seconds, and appears in "+ str(number_of_scenes_with_the_emotion)+" scenes.")
        else:
            print("Sorry, this emotion was not found")
       