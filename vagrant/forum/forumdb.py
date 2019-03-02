# "Database code" for the DB Forum.

import datetime
import psycopg2
import sqlite3

db = sqlite3.connect('forum.sqlite')
cur = db.cursor()


POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  cur.execute("select time, content from posts")
  return cur.fetchall()
  

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  cur.execute("insert into posts (content) values (?)", (content,))
  db.commit()

