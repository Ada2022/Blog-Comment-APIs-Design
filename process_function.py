import sqlite3
import pandas as pd
from datetime import datetime
import argparse


def initDB(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blogs (
        id INTEGER PRIMARY KEY,
        blog_id INTERGER NOT NULL,
        author TEXT NOT NULL,
        content TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        blog_id INTEGER NOT NULL,
        author TEXT NOT NULL,
        time_stamp TEXT NOT NULL,
        content TEXT NOT NULL,
        FOREIGN KEY (blog_id) REFERENCES blogs(blog_id)
    )
    """)
    conn.commit()


def add_comment(conn, blog_id, author, content):
    cursor = conn.cursor()

    blog_exist = pd.read_sql_query(
        "SELECT blog_id FROM blogs WHERE blog_id = ? ", conn, params=(blog_id, ))
    if blog_exist.empty:
        print("Blog doesn't exist, cannot comment")
        return False

    last_id = pd.read_sql_query(
        "SELECT id FROM comments", conn) 
    last_id = -1 if last_id.empty else last_id.index[-1]


    cursor.execute("""
    INSERT INTO comments (id, blog_id, author, time_stamp, content)
    VALUES (?, ?, ?, ?, ?)
    """, (last_id + 1, blog_id, author, datetime.now().strftime('%Y-%m-%d %H:%M'), content))

    conn.commit()
    return True


def show_comment(conn, blog_id=None, author=None, time_stamp=None):
    query = "SELECT * FROM comments"
    conditions = []
    params = []
    if author is not None:
        conditions.append("author = ?")
        params.append(author)
    if blog_id is not None:
        conditions.append("blog_id = ?")
        params.append(blog_id)
    if time_stamp is not None:
        conditions.append("time_stamp = ?")
        params.append(time_stamp)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor = conn.cursor()
    cursor.execute(query, params)
    comments = cursor.fetchall()

    if len(comments) == 0:
        print("No matching comments")
    else:
        print("\nComments:")
        for comment in comments:
            print(comment)
    return comments


def delete_comment(conn, blog_id=None, author=None, time_stamp=None):
    query = "DELETE FROM comments"
    conditions = []
    params = []
    if author is not None:
        conditions.append("author = ?")
        params.append(author)
    if blog_id is not None:
        conditions.append("blog_id = ?")
        params.append(blog_id)
    if time_stamp is not None:
        conditions.append("time_stamp = ?")
        params.append(time_stamp)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()


def add_blog(conn, blog_id, author, content):
    cursor = conn.cursor()

    last_id = pd.read_sql_query(
        "SELECT blog_id FROM blogs", conn)
    last_id = -1 if last_id.empty else last_id.index[-1]

    cursor.execute("""
    INSERT INTO blogs (id, blog_id, author, content)
    VALUES (?, ?, ?, ?)
    """, (last_id + 1, blog_id, author, content))

    conn.commit()


def show_blog(conn, blog_id=None, author=None):
    query = "SELECT * FROM blogs"
    conditions = []
    params = []
    if blog_id is not None:
        conditions.append("blog_id = ?")
        params.append(blog_id)
    if author is not None:
        conditions.append("author = ?")
        params.append(author)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor = conn.cursor()
    cursor.execute(query, params)
    blogs = cursor.fetchall()
    if len(blogs) == 0:
        print("No matching blogs")
    else:
        print("\nBlogs:")
        for blog in blogs:
            print(blog)
    return blogs


def process_args(args):
    db = args.database_name
    conn = sqlite3.connect(db)

    initDB(conn)
    if args.command == "add-blog":
        add_blog(conn, args.blog_id, args.author, args.content)
    elif args.command == "show-blog":
        show_blog(conn, blog_id=args.blog_id, author=args.author)
    elif args.command == "add-comment":
        add_comment(conn, args.blog_id, args.author, args.content)
    elif args.command == "delete-comment":
        delete_comment(conn, blog_id=args.blog_id,
                       author=args.author, time_stamp=args.time_stamp)
    elif args.command == "show-comment":
        show_comment(conn, blog_id=args.blog_id,
                     author=args.author, time_stamp=args.time_stamp)
    else:
        print("Invalid command")

    conn.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Blog Comment System")
    parser.add_argument('--database_name', default="blogs.db",
                        help="please enter database name")
    parser.add_argument("command", choices=[
                        "add-blog", "add-comment", "delete-comment", "show-comment", "show-blog"], help="Action to be taken")
    parser.add_argument("--blog-id", type=int, help="Blog ID")
    parser.add_argument("--author", help="Author of the blog/comment")
    parser.add_argument("--content", help="Content of the blog/comment")
    parser.add_argument("--time-stamp", help="Time stamp of the comment")
    args = parser.parse_args()
    process_args(args)
