import glob
import os
import sys
import traceback
from twython import TwythonStreamer
from twython import Twython
import requests
import imageio
import cv2
from slackclient import SlackClient
from run import run_sim


# Auth
with open("credentials.txt") as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()
    try:
        slack_token = f.readline().strip()
    except:
        pass

twitter = Twython(consumer_key, consumer_secret,
                  access_token, access_token_secret)
sc = SlackClient(slack_token)

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
class MyStreamListener(TwythonStreamer):
    def on_success(self, status):
        try:
            id_str = status['id_str']
            text_ = status['text']
            sender_ = status['user']['screen_name']
            print("============================================")
            print("Recieved tweet from {}".format(sender_))

            media_url = status['entities']['media'][0]['media_url_https']
            print("Image URL is {}".format(media_url))

            # Download and save image
            path = "server/in/"
            filename = str(id_str) + '.jpeg'
            f = open(path + filename, 'wb')
            f.write(requests.get(media_url).content)
            f.close()

            # Call the simulation on this downloaded file
            # This should result on several images placed in /server/output
            print("Started simulation")
            run_sim(path + filename)

            # Generate GIF
            print("Creating GIF")
            create_gif(sorted(glob.glob('server/out/{}*.png'.format(id_str))), 0.15)

            # Tweet back with the image!
            print("Tweeting back")
            photo = open('server/out/{}.gif'.format(str(id_str)), 'rb')
            response = twitter.upload_media(media=photo)
            message = "Here is the simulation in your image! @{}".format(sender_)
            twitter.update_status(status=message, media_ids=[response['media_id']],
                                  in_reply_to_status_id=id_str)
            print("All done successfully!")

        except:
            error = traceback.format_exc()
            print("TRACEBACK:")
            print(error)

            sc.api_call(
                "chat.postMessage",
                channel="twitter-fluid-flow",
                text=str(error)
            )

        print()

if __name__ == "__main__":
    myStream = MyStreamListener(consumer_key, consumer_secret,
                              access_token, access_token_secret)

    myStream.statuses.filter(track='@FluidFlowTest')
