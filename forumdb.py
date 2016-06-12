#
# Database access functions for the web forum.
# 

import time
import psycopg2

import bleach;

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    conn = psycopg2.connect("dbname=forum")
    c = conn.cursor()
    c.execute('select content, time from posts')
    records = c.fetchall()
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in records]
    posts.sort(key=lambda row: row['time'], reverse=True)
    conn.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    conn = psycopg2.connect("dbname=forum")
    c = conn.cursor()
    t = time.strftime("%c", time.localtime())
    c.execute('insert into posts (content, time) values(%s, %s)', (content, t,))
    conn.commit()
    conn.close()
