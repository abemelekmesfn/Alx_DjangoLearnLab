# API View Setup in advanced_api_project

## Book Views Overview

- **BookListView**: `/api/books/` — Public access to list all books.
- **BookDetailView**: `/api/books/<id>/` — Public access to retrieve a book by ID.
- **BookCreateView**: `/api/books/create/` — Authenticated users only. Adds a new book.
- **BookUpdateView**: `/api/books/<id>/update/` — Authenticated users only. Updates a book.
- **BookDeleteView**: `/api/books/<id>/delete/` — Authenticated users only. Deletes a book.

## Permissions

- `IsAuthenticated` used to protect create/update/delete endpoints.
- `AllowAny` used for listing and retrieving books.

## Custom Behavior

- The `BookSerializer` includes validation to ensure `publication_year` is not in the future.
- `perform_create()` method can be overridden to log or customize save behavior.

## API Query Parameters

### 🔎 Filtering
- `/api/books/?title=1984`
- `/api/books/?author=1`
- `/api/books/?publication_year=1949`

### 🔍 Searching
- `/api/books/?search=Orwell` → Searches `title` and `author.name`

### 🔃 Ordering
- `/api/books/?ordering=title` → Ascending by title
- `/api/books/?ordering=-publication_year` → Descending by year

### ✅ Example Combined:
`/api/books/?search=Orwell&ordering=-publication_year`

## 🧪 Running Tests

### How to Run Tests:
```bash
python manage.py test api
