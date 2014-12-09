import praw, cPickle
from collections import Counter

r = praw.Reddit(user_agent='getting political stuff')
r.login('jacobeisenstein','cssisathing')

linebreak = '-----==----==---==-----'

# this may take a while. start early.
def getThreads(subreddit,num_comments=10,max_threads=500,min_comments=10,max_comments=1000,verbose=False):
    comment_counter = 0
    already_done = [] #keep track of threads you've already seen (you can get them twice)
    subred = r.get_subreddit(subreddit) #get a subreddit
    with open('.'.join([subreddit,'txt']),'w') as fout:
        while comment_counter < num_comments:# len(threads) < num_threads:
            #you could try alternatives to get_top_from_year
            for sub in subred.get_new(limit=max_threads):
                if sub.id not in already_done and comment_counter < num_comments:
                    already_done.append(sub.id)
                    sub.replace_more_comments(limit=None, threshold=0)
                    for comment in sub.comments:                        
                        print >>fout, comment.body.encode('utf-8')
                        print >>fout, linebreak
                        print '.',
                        comment_counter += 1
    print ""

thread_names = ['Libertarian','Conservative','Progressive','Socialism','Anarchism']

for thread_name in thread_names:
    print thread_name,
    getThreads(thread_name,num_comments=1000,max_comments=100,min_comments=0,verbose=True)
