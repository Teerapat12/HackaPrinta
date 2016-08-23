from PIL import Image
import cv2
import pickle
import os

#load loaded_picture list and framed_picture list


with open("loaded_pics.txt", 'rb') as f:
    loaded_pics = pickle.load(f)

with open("framed_pics.txt", 'rb') as f:
    framed_pics = pickle.load(f)


print(framed_pics)

ig_frame = cv2.imread("igframe.jpg")
x_offset=93
y_offset=269

while True:
    for file in os.listdir("Loaded_Picture"):
        if file.endswith(".jpg") and not (any(file in s for s in framed_pics)):
            print("Printing",file)
            s_img = cv2.imread("Loaded_Picture/"+file)
            s_img = cv2.resize(s_img,(620,560))
            ig_frame[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
            cv2.imwrite('Framed_Picture/'+file,ig_frame)
            framed_pics.append(file)
            with open("framed_pics.txt", 'wb') as f:
                    pickle.dump(framed_pics, f)





#img = Image.open('Loaded_Picture/time.teerapat_17850980950099122.jpg') # image extension *.png,*.jpg

#img = img.resize((new_width, new_height), Image.ANTIALIAS)
#img.save('Framed_Picture/time.teerapat_blabla.jpg') # format may what u want ,*.png,*jpg,*.gif
