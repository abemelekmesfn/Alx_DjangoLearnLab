# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- `can_view`: view books
- `can_create`: create books
- `can_edit`: edit books
- `can_delete`: delete books

## Groups and Their Permissions
- **Admins**: All permissions
- **Editors**: `can_create`, `can_edit`
- **Viewers**: `can_view`

## Views
- `view_books`: Requires `can_view`
- `create_book`: Requires `can_create`
- `edit_book`: Requires `can_edit`
- `delete_book`: Requires `can_delete`

## How to Assign
Use Django admin to assign users to groups. Permissions are automatically checked using decorators.
