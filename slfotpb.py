from secrets import *
import logging
import json
import time
import os
import requests
import tweepy
from PIL import Image, ImageDraw, ImageFilter


logging.basicConfig(level=logging.INFO, filename='/code/app.log', format='%(asctime)s - %(message)s')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

# try:
#     api.verify_credentials()
#     logging.info("Authentication OK")
# except:
#     logging.ERROR("Authentication Error")


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    pil_img = pil_img.resize((150, 150), resample=0, box=None)
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    result = pil_img.copy()
    result.putalpha(mask)
    return result


def create_banner():
    offset = 575
    banner_image = Image.open('/code/banner.jpg')
    header_image = banner_image.copy()
    for filename in os.listdir('.'):
        if not (filename.endswith('.jpg')) or filename == 'banner.jpg' or filename == 'header-image.jpg':
            continue
        img = Image.open(filename)
        img_thumb = mask_circle_transparent(img, 0)
        header_image.paste(img_thumb, (offset, 250), img_thumb)
        offset += 200
    header_image.save('header-image.jpg')


def update_profile_banner(filename):
    api.update_profile_banner(filename)

followers = tweepy.Cursor(api.get_followers).items(3)

profile_image_url = []
for f in followers:
    profile_url = f.profile_image_url_https.replace('_normal', '')
    profile_image_url.append(profile_url)

for url in profile_image_url:
    response = requests.get(url)
    with open('img' + str(profile_image_url.index(url)) + '.jpg', 'wb') as f:
        f.write(response.content)

create_banner()
update_profile_banner('header-image.jpg')
logging.info('profile banner updated successfully')