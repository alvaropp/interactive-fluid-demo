import glob
import os
import tweepy
import requests
import imageio
import cv2
from run import run_sim


# Auth
with open("credentials.txt") as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Generate GIF. Based on:
# http://www.idiotinside.com/2017/06/06/create-gif-animation-with-python/
def create_gif(filenames, duration):
    outputName = filenames[0].split("_")[0]
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = "{}.gif".format(outputName)
    imageio.mimsave(output_file, images, duration=duration)

# Stream
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        id_ = status.id
        text_ = status.text
        sender_ = status.user.screen_name
        print("============================================")
        print("Recieved tweet from {}".format(sender_))

        try:
            media_url = status.entities['media'][0]['media_url_https']
            print("Image URL is {}".format(media_url))

            # Download and save image
            path = "server/in/"
            filename = str(id_) + '.jpeg'
            f = open(path + filename, 'wb')
            f.write(requests.get(media_url).content)
            f.close()

            # Call the simulation on this downloaded file
            # This should result on several images placed in /server/output
            print("Started simulation")
            run_sim(path + filename)

            # Generate GIF
            print("Creating GIF")
            create_gif(sorted(glob.glob('server/out/{}*.png'.format(id_))), 0.15)

            # Tweet back with the image!
            print("Tweeting back")
            filename = "server/out/{}.gif".format(str(id_))
            message = "Here is the simulation in your image! @{}".format(sender_)
            api.update_with_media(filename, status=message, in_reply_to_status_id=id_)

            # Trying to clean everything
            # print("Attempting to clean things up")
            # cv2.destroyAllWindows()
            # cv2.waitKey(1)
            # cv2.waitKey(1)
            # cv2.waitKey(1)
        except:
            pass

        print()

if __name__ == "__main__":
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['@FluidFlowTest'], async=True)
