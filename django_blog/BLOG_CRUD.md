 Features
  List all posts (`/posts/`)
  View a single post (`/posts/<id>/`)
  Create new post (logged-in users only)
  Edit and delete posts (only author can)

 Class-Based Views Used
  ListView: `PostListView`
  DetailView: `PostDetailView`
  CreateView: `PostCreateView`
  UpdateView: `PostUpdateView`
  DeleteView: `PostDeleteView`

Permissions
 Create/Edit/Delete: Requires login
 Update/Delete: Only post authors can
 View/List: Publicly accessible

Testing
Ensure:
 Unauthorized users can't create/edit/delete
 Only authors can modify their own posts
 All templates and links work correctly