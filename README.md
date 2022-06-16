# slfotpb
Show the latest followers on your Twitter profile banner image, using Twitter API.


This idea was inspired by [Tony Dinh](https://twitter.com/tdinh_me) on twitter,
although his app has lots of features and is much nicer. If you are not following him, please do.
See my profile banner [here](https://twitter.com/VTaghiloo). This code is not always running 
on a server yet, but you might be lucky and see your profile picture on my profile banner image.

# How it works
The python code communicates with Twitter through Twitter API with the help of [tweepy](https://github.com/tweepy/tweepy) library. It then fetches the latest 3 followers' profile pictures and makes a banner image. Finally it updates the banner on your profile. The whole code can be packaged as a docker image which a cronjob runs the code every 2 minutes.

# important notice
In order to use the code you need a Twitter developer account and must fill the secrets.py file with the required tokens and keys. Getting a Twitter developer account for personal usage is simple. Just email Twitter with a brief explanation and ask for an account. Without the keys the code will not work. 

# The way I run it:
use any name for <tag> and <container_name>

```
$ docker image build -t <tag> .
$ docker run -d -it --name <container_name> --mount type=bind,source=/temp/app.log,target=/code/app.log <tag>
```

# To Do:
+ multistage Dockerfile
+ optimize Dockerfile to decrease image size
+ add other features (for instance like or scrape tweets based on hashtags)
+ find a better way to log the output

