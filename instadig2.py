from instagram import client, subscriptions
import urllib2
import sys
import time


# CONFIGURATION
CONFIG = {
    'client_id': 'YOUR ID HERE'
    'client_secret': 'YOUR SECRET HERE'
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

download_max = 1500

api = client.InstagramAPI(**CONFIG)
tag = sys.argv[1]
nextID = sys.argv[2]

downloads = 0

while downloads < download_max:
    print 'downloaded ' + str(downloads) + '/' + str(download_max)
    tries = 0

    while tries < 3:
        try:
            recent_media, next = api.tag_recent_media(25, nextID, tag)
            break
        except:
            print 'try ' + str(tries) + ': api call failed. trying again in 1s'
            tries = tries + 1
            time.sleep(1)

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
                print 'try ' + str(tries) + ': api call failed. trying again in 1s'
                tries = tries + 1
                time.sleep(1)

        imgOutput = open(name + '.jpg', 'wb')
        imgOutput.write(nextfile.read())
        imgOutput.close()
        
        downloads = downloads + 1
    
    print 'calling with nextID: ' + nextID
