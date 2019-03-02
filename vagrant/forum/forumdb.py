# "Database code" for the DB Forum.

import datetime
import sqlite3

# db = sqlite3.connect("forum.sqlite")


POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = sqlite3.connect("forum.sqlite")
  cur = db.cursor()
  cur.execute('''select content, time from posts''')
  return cur.fetchall()
  

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = sqlite3.connect("forum.sqlite")
  cur = db.cursor()
  cur.execute('''insert into posts (content) values (?)''', (content,))
  db.commit()
  db.close()

