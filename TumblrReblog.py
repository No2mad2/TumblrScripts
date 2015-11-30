import pytumblr, json, random, time
from random import randint

client = pytumblr.TumblrRestClient(
  'xxx',
  'xxx',
  'xxx',
  'xxx'
)

tags = ['tag1', 'tag2', 'tag3', 'tag(n)']

# Count how many posts we reblog
x = 0

while True: #Continue indefinitely
    randomtag = (random.choice(tags)) #Randomly pick a tag from the above list
    print randomtag
    print 'REBLOG KEY %s' % (client.tagged(randomtag)[0]['reblog_key']) #For debugging purposes, reblog key is printed
    reblogkey = (client.tagged(randomtag)[0]['reblog_key'])

    print 'ID %s' % (client.tagged(randomtag)[0]['id'])
    postid = (client.tagged(randomtag)[0]['id'])

    client.reblog('YOURBLOGNAMEHERE.tumblr.com', id=postid, reblog_key=reblogkey)
    print 'reblogged!'
    
    print "Rolling Like dice"
    diceroll = (randint(0,2)) #Randomly like posts in addition to reblogging them
    print 'rolled a %s' % diceroll
    if diceroll == 1:
        client.like(postid, reblogkey)
        print "post liked!"
        
    x += 1
    print 'posts reblogged so far: %s' % x #Print how many posts we've reblogged
    
    
    #timerand = (randint(300, 600))
    timerand = (randint(700, 1500)) #Wait for some time to reduce spam
    print 'sleeping for %s' % (timerand)
    time.sleep(timerand)



