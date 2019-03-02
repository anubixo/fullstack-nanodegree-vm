# "Database code" for the DB Forum.

import datetime
import psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database='forum')
  c = db.cursor()
  c.execute("select * from posts")
  POSTS = c.fetchall()
  c.close()
  db.close()
  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database='forum')
  c = db.cursor()
  c.execute("insert into posts (content) values ('%s')" % content)
  db.commit()
  db.close()


