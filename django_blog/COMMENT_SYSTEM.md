 Features
 Users can leave comments on blog posts
 Authenticated users can:
   Post new comments
   Edit or delete their own comments
 Comments are shown on each post's detail page

 Models
 `Comment`: Links to `Post` and `User`, includes content and timestamps

 Permissions
 Only authenticated users can add comments
 Only the comment author can edit or delete