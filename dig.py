from instagram import client, subscriptions
import urllib2
import sys

CONFIG = {
    'client_id': '5b8ae8f010d64112a48f969b6af736d5',
    'client_secret': '6cdf09f8c92644f68d6846000880752e',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

api = client.InstagramAPI(**CONFIG)
tag = sys.argv[1]
nextID = ''

while True:
    recent_media, next = api.tag_recent_media(25, nextID, tag)
    nextID = next.split('=')[-1]
    print 'found ' + str(len(recent_media)) + ' new items'

    for media in recent_media:
        name = str(media).replace('Media: ','')
        print 'downloading ' + name
        
        jsonOutput = open(name + '.json', 'wb')
        jsonOutput.write(str(vars(media)))
        jsonOutput.close()

        nextfile = urllib2.urlopen(media.images['standard_resolution'].url)
        imgOutput = open(name + '.jpg', 'wb')
        imgOutput.write(nextfile.read())
        imgOutput.close()
    
    print 'calling with nextID: ' + nextID
