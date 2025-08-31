Social Media Api

Set up Instructions

  Install dependencies
  Run migrations
  Start server
  `POST /api/accounts/register/` - Create a new user and get token
 `POST /api/accounts/login/` - Log in and get token
 `GET /api/accounts/profile/` - View profile (Auth required)

 User Model Fields
 `username`, `email`, `bio`, `profile_picture`, `followers`

Posts API
List Posts
`GET /api/posts/`  
Supports pagination and search:  
`/api/posts/?search=title`

Create Post
`POST /api/posts/`  
Headers: `Authorization: Token <token>`  
Body:
```json
{
  "title": "My Post",
  "content": "Post content here"
}

Follow System

Follow a User
`POST /api/accounts/follow/<user_id>/`  
Headers:

Like System

Like a Post
`POST /api/posts/<post_id>/like/`
Headers:

