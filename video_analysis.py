import cv2  # this is required!
import numpy as np 
np.set_printoptions(legacy='1.25')

# Make sure the video file name matches the one you just put in the folder
video_to_open=input("Enter the file of the video you want to enter:")
video_path = f"Scripts/{video_to_open}"  # replace with your video file name


# Open the video
hehe = cv2.VideoCapture(video_path)


if not hehe.isOpened():
   print("Error: Could not open video.")
   exit()


# Get video info
frame_count = int(hehe.get(cv2.CAP_PROP_FRAME_COUNT))
fps = hehe.get(cv2.CAP_PROP_FPS)
duration = frame_count / fps


print("Video opened successfully!")
print("Total frames:", frame_count)
print("FPS:", fps)
print("Duration (seconds):", round(duration, 2))
count=1
variation_of_mean_pixel=[]
my_previous_intensity=0
while True:
   ret,frame=hehe.read()
   if not ret: 
      print("End of video or read error.")
      break
   if ret==True:
      my_gray_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Method that allows to convert the color space of an image, can covert between different types. 
      average_intensity=np.mean(my_gray_frame)
      rounded=round(average_intensity,2)
      print("Frame",count,"has mean pixel value",rounded)
   if count==10:
      break 
   my_current_intensity=rounded
   difference=my_previous_intensity-my_current_intensity
   difference=round(difference,2)
   variation_of_mean_pixel.append(difference)
   count+=1
   my_previous_intensity=my_current_intensity
##Trying the same thing but grouped by every 10 seconds.
hehe.set(cv2.CAP_PROP_POS_FRAMES,0)
frames_in_ten_seconds=round(fps*10,0)
frames_in_ten_seconds=int(frames_in_ten_seconds)
video_finished=False
ten_second_window_number=1
difference_between_ten_second_things=[]
##Have now finished defining some controls

while not video_finished:
   average_of_ten_seconds=0
   my_sum=0
   my_counter=0
   print("Processing 10-second window",ten_second_window_number)
   while my_counter<frames_in_ten_seconds:
      ret,frame=hehe.read()
      if not ret:
         video_finished=True
         break
     
      my_gray_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      average_intensity=np.mean(my_gray_frame)
      my_sum=average_intensity+my_sum
      my_counter+=1
   
   if my_counter>0:
      average_of_ten_seconds=round(my_sum/my_counter,2)
      print("Average intensity:",average_of_ten_seconds)
   difference_between_ten_second_things.append(average_of_ten_seconds)
   ten_second_window_number+=1
##Now trying average
hehe.set(cv2.CAP_PROP_POS_FRAMES, 0)
average_colors=[]
frame_count2=0
blue_sum=0
green_sum=0
red_sum=0
sum

while True:
   ret,frame=hehe.read()
   if not ret:
      #print(f"Finished processing {frame_count2} frames. Exiting loop.")
      break
   
   average_color_per_frame=np.average(np.average(frame,axis=0),axis=0)
   #Result of this is a numpy array that has B,G,R values
   blue_mean_for_this_frame=average_color_per_frame[0]
   green_mean_for_this_frame=average_color_per_frame[1]
   red_mean_for_this_frame=average_color_per_frame[2]
   blue_sum= blue_mean_for_this_frame+blue_sum
   green_sum=green_mean_for_this_frame+green_sum
   red_sum=red_mean_for_this_frame+red_sum
   frame_count2=frame_count2+1 

average_blue=blue_sum/frame_count2
average_blue=int(round(average_blue,0))
average_green=green_sum/frame_count2
average_green=int(round(average_green,0))
average_red=red_sum/frame_count2
average_red=int(round(average_red,0))

average_color_square=np.full((200,200,3),(average_blue,average_green,average_red),dtype=np.uint8)

average_colors_split=(average_red,average_green,average_blue)
print("The average colors in format RGB are:",average_colors_split)
cv2.imshow("Average Color of the Film", average_color_square)
cv2.waitKey(0)
cv2.destroyAllWindows()



print(variation_of_mean_pixel)
print("String that shows differences in brightness in 10 second windows",difference_between_ten_second_things)
hehe.release()


