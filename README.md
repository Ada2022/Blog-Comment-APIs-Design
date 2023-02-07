# Blog-Comment-APIs-Design

​        This is a Python based system for managing blogs and comments in a SQLite database. The system is built using the `sqlite3` and `pandas` libraries and provides functionalities for adding, showing and deleting blogs and comments. 

​        To test our apis, we built a local website with `flask` and visualize our database.

## Requirements

- Python 3.x

- sqlite3

- pandas

- datetime

- argparse

- flask

## Usage

1. Clone code in your folder
   
   ```shell
   git clone https://github.com/Ada2022/Blog-Comment-APIs-Design.git
   ```

2. Run app.py
   
   ```shell
   cd Blog-Comment-APIs-Design-master/Blog-Comment-APIs-Design-master
   python app.py
   ```

3. View comments and blogs history in localhost
   
   ```shell
   # After running app.py, you'll see the following note, CTRL and left click the link 
   Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

## Detailed Function

Five functions are implemented on this repo.

1. #### add-blog-api     `method: POST endpoint: /`
   
   **Description:** This command create a blog record in TABLE "blogs" in your database. You need to specific blog_id, author and content to create a valid blog.
   
   **Parameters：**
   
   * blog_id (optional, integer): The id of blog which you comment on
   * author(optioal): The author of the comment
   * content: The time you comment 
   
   **Response:** 
   
   * message: if sucessfully added, the message is "Blog Added" 
   * return_code: if sucessfully added, return_code is 200
   
   **Shell Usage:**
   
   Function select add blog, enter blog_id, author and content respectively, and click submit on the website
   OR
   
   ```bash
   >>> python process_function.py add-blog --blog-id <id>--author <author> --content <content>
   ```

2. #### show-blog-api     `GET /`
   
   **Description:** This command will show blogs which satisfy given constraints. By default, it will display all blogs. You could filter them by specific blog_id. If no blog satisfy given constrains, you'll get "No matching blogs"
   
   **Parameters：**
   
   * blog_id (optional, integer): The id of blog which you comment on
   
   **Response:** 
   
   * data(list): Blogs that satisfy given requirements. 
   
   **Usage:**
   
   Function select show blog, enter blog_id (optional), and click submit on the website
   
   OR
   
   ```bash
   >>> python process_function.py show-blog --blog-id <id>[optional] --author <author>[optional] --content <content>[optional]
   ```

3. #### add-comment-api    `POST /`
   
   **Description**: This command create a comment record in TABLE "comments" in your database. You need to specific blog_id, author and content to create a valid comment. Note that you can only comment under an existing blog. 
   
   **Parameters：**
   
   * blog_id: The id of blog which you comment on
   * author: The author of the comment
   * content: The time you comment 
   
   **Response:** 
   
   * blog_exit_flag(bool): if sucessfully added, the flag is True.
   
   **Shell Usage:**
   
   Function select add comment, enter blog_id, author and content respectively, and click submit on the website
   OR
   
   ```shell
   >>> python process_function.py add-comment --blog-id <id> --author <author> --content <content>[optional]
   ```

4. #### delete-comment-api    `DELETE /`
   
   **Description:** This API will delete comments with given constraints. You need specific at least one argument(blog_id and author) to tell which comment should be deleted.
   
   **Parameters：**
   
   * blog_id (optional, integer): The id of blog which you comment on
   * author(optioal): The author of the comment 
   
   **Response:** 
   
   * message: if sucessfully deleted, the message is "Comment Deleted" 
   * return_code: if sucessfully deleted, return_code is 200
   
   **Shell Usage:**
   
   Function select delete comment, enter blog_id (optional) and author (optional) respectively, and click submit on the website
   OR
   
   ```shell
   >>> python process_function.py delete-comment --blog-id <id>[optional] --author <author>[optional] --content <content>[optional]
   ```

5. #### show-comment-api     `GET /`
   
   **Description:** This command will show blogs which satisfy given constraints. By default, it will display all blogs. You could filter them by specific blog_id and author.  If no comment satisfy given constrains, you'll get "No matching comments"
   
   **Parameters：**
   
   * blog_id (optional, integer): The id of blog which you comment on
   * author(optioal): The author of the comment
   
   **Response:** 
   
   * data(list): Comments that satisfy given requirements. 
   
   **Shell Usage:**
   
   Function select show comment, blog_id (optional) and author (optional) respectively, and click submit on the website
   
   OR
   
   ```shell
   >>> python process_function.py show-comment --blog-id <id>[optional] --author <author> [optional] --content <content>[optional]
   ```

## Example Video

```html
<video id="video" controls="" preload="auto">
    <source id="mp4" src="/demo.mp4" type="video/mp4">
</video>
```