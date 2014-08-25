from instagram import client, subscriptions
import urllib2
import sys
import time

CONFIG = {
    'client_id': '5b8ae8f010d64112a48f969b6af736d5',
    'client_secret': '6cdf09f8c92644f68d6846000880752e',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

api = client.InstagramAPI(**CONFIG)
tag = sys.argv[1]
nextID = sys.argv[2]

while True:
    try:
        tries = 0

        while tries < 3:
            try:
                recent_media, next = api.tag_recent_media(25, nextID, tag)
                break
            except:
                'api call failed. trying again in 3.'
                tries = tries + 1
                time.sleep(3)

        nextID = next.split('=')[-1]
        print 'found ' + str(len(recent_media)) + ' new items'

        for media in recent_media:

            name = str(media).replace('Media: ','')
            
            print 'downloading ' + name
            jsonOutput = open(name + '.json', 'wb')
            jsonOutput.write(str(vars(media)))
            jsonOutput.close()
           
            tries = 0
            while tries < 3:
                try:
                    nextfile = urllib2.urlopen(media.images['standard_resolution'].url, None, 5)
                    break
                except:
                    print 'try failed. trying again in 2.'
                    tries = tries + 1
                    time.sleep(2)

            imgOutput = open(name + '.jpg', 'wb')
            imgOutput.write(nextfile.read())
            imgOutput.close()

        print 'calling with nextID: ' + nextID

    except:
        continue