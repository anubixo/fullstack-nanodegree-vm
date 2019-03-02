# "Database code" for the DB Forum.

import datetime
import psycopg2

conn = psycopg2.connect("dbname=forum")
cur = conn.cursor()



POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  cur.execute("select * from posts")
  POSTS = cur.fetchall()
  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  cur.execute("insert into posts (content) values (%s)", content)

cur.close()
conn.close()
