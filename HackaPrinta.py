print("OH yeah HACKA PRINTA")
from instagram.client import InstagramAPI
import urllib
import os
import pickle
from PIL import Image

client_id = "af9c8917403548f6a411f619353a2972"
access_token = "2188998620.af9c891.fc995123731946bdb327bb761250eca5"
client_secret = "e19dfb00108f4aa687d5ac2699c45f24"
user_id = "2188998620"
tag_name = "cat" # some tag

#How to Fix module bug : http://stackoverflow.com/questions/33924581/keyerror-data-with-python-instagram-api-client
#Example json : https://api.instagram.com/v1/tags/cat/media/recent?access_token=2188998620.af9c891.fc995123731946bdb327bb761250eca5&count=10

#TODO: upgrade access_token so that it can look at the hashtag from everyone uploaded pic

api = InstagramAPI(client_id=client_id, client_secret=client_secret,access_token=access_token)

api.tag(tag_name) 




#Reset loaded pics in text file
#with open("loaded_pics.txt", 'wb') as f:
    #pickle.dump([], f)

with open("loaded_pics.txt", 'rb') as f:
    loaded_pics = pickle.load(f)

while True:
    tag_recent_media, next_ = api.tag_recent_media(tag_name="cat",count=100)
    for media in tag_recent_media:
        if not (any(media.id in s for s in loaded_pics)):
            print media.caption.text
            print media.images["standard_resolution"].url
            urllib.urlretrieve(media.images["standard_resolution"].url, "Loaded_Picture/"+media.user.username+"_"+media.caption.id+".jpg")
            loaded_pics.append(media.id)
            with open("loaded_pics.txt", 'wb') as f:
                pickle.dump(loaded_pics, f)


#TODO:put picutre in frame here?

#TODO:save as new pic in finished folder




print "----------------"
urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

