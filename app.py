import os
from process_function import *
from flask import Flask, request, render_template

DB_FILE = "./blogs.db"
app = Flask('myApp')


@app.route("/", methods=["GET", "POST", "DELETE"])
def home():
    if request.method == "POST" or request.method == "GET":
        blog_id = request.form.get('blog_id')
        author = request.form.get('author')
        content = request.form.get('content')
        function = request.form.get('function')

        if function == 'add_blog':
            add_blog_api(blog_id, author, content)
            return "Blog added successfully. Please click the arrow in the upper left corner to return to the main interface"
        elif function == 'show_blog':
            data = show_blog_api(blog_id)
            return render_template("./home.html", function=function, data=data)
        elif function == 'add_comment':
            blog_exit_flag = add_comment_api(blog_id, author, content)
            if blog_exit_flag:
                return "Comment added successfully. Please click the arrow in the upper left corner to return to the main interface"
            else:
                return "Blog you want to comment on does not exist. Please check the Blog ID"
        elif function == 'show_comment':
            data = show_comment_api(blog_id, author)
            return render_template("./home.html", function=function, data=data)
        elif function == 'delete_comment':
            delete_comment_api(blog_id, author)
            return "Comment deleted successfully. Please click the arrow in the upper left corner to return to the main interface"

    return render_template("./home.html")


@app.route("/", methods=["POST"])
def add_blog_api(blog_id, author, content):
    conn = sqlite3.connect(DB_FILE)
    add_blog(conn, blog_id, author, content)
    return "Blog Added", 200


@app.route("/", methods=["GET"])
def show_blog_api(blog_id):
    blog_id = request.args.get("blog_id")
    conn = sqlite3.connect(DB_FILE)
    data = show_blog(conn, blog_id=blog_id)
    return data


@app.route("/", methods=["POST"])
def add_comment_api(blog_id, author, content):
    conn = sqlite3.connect(DB_FILE)
    blog_exit_flag = add_comment(conn, blog_id, author, content)
    return blog_exit_flag


@app.route("/", methods=["GET"])
def show_comment_api(blog_id, author):
    blog_id = request.args.get("blog_id")
    author = request.args.get("author")
    conn = sqlite3.connect(DB_FILE)
    data = show_comment(conn, blog_id, author)
    return data


@app.route("/", methods=["DELETE"])
def delete_comment_api(blog_id, author):
    if len(blog_id) == 0:blog_id = None
    if len(author) == 0:author = None  
    print("hey", blog_id, author)
    conn = sqlite3.connect(DB_FILE)
    delete_comment(conn, blog_id, author)
    return "Comment Deleted", 200


if __name__ == "__main__":
    database_path = "./blogs.db"
    if not os.path.exists(database_path):
        conn = sqlite3.connect(DB_FILE)
        initDB(conn)
        print("DB initialized.")
        app.run()
        conn.close()
    else:
        app.run()
