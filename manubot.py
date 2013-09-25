#!/usr/bin/python
# Reddit ManU downvote bot, v1.0
# rostislav.tsiomenko@gmail.com
# Note this is probably unethical
import praw
import time

# Create PRAW object, login, open comments already voted on
r = praw.Reddit(user_agent='Muck FanU v1.0')
r.login('MuckFanU', 'beepbeep')
votes = open('votes.txt', 'a+')
voted = votes.read().splitlines()

# Loop through front page submissions on /r/soccer
subreddit = r.get_subreddit('soccer')
for submission in subreddit.get_hot(limit=25):
    comments = submission.all_comments_flat
    # Check if comment has been voted on, down/up vote
    for comment in comments:
        cid = comment.id
        if cid not in voted:
            # Determine team by getting user flair
            team = comment.author_flair_css_class
            if team == "man-utd":
                comment.downvote()
                votes.write(cid + '\n')
                print "Comment ID " + cid + " downvoted!"
                time.sleep(3)
            elif team == "arsenal":
                comment.upvote()
                votes.write(cid + '\n')
                print "Comment ID " + cid + " upvoted!"
                time.sleep(3) 
        else:
            print "Comment ID " + cid + " has already been voted on, skipping.."
    
    # Extra pause for API limit
    time.sleep(10)     
votes.close()

