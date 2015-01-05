InstaDig
=========

Download Instagram images and metadata by hashtag.
To start:

```
itu@home:~> python instadig.py justinbieber 0
downloaded 0/1500
found 25 new items
downloading xcKsJ2Avv5
downloading xaRn8Vgvvb
...
```

To continue where you left off: 
`python justinbieber xaRn8Vgvvb`

After downloading a huge amount of images, the amount of files causes `mv` and other utils problems.
`splitter.sh`divides the files in folders of 1000 each.
