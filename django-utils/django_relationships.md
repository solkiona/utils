# Django Model Relationships: One-to-One, Many-to-Many, Foreign Key, and Filtering Methods

## One-to-One Relationships

In Django, a one-to-one relationship is represented using `OneToOneField`. This is useful when each instance of a model should be associated with only one instance of another model. A One-to-One relationship allows traversal back and forth between related models seamlessly. The reason you can do `user.profile.bio`, even though the User model does not explicitly have a profile field, is due to Django's reverse relation mechanism.

## How Does This Work?
When you define a OneToOneField, Django automatically creates a reverse relation from the related model back to the primary model. This reverse relation is accessible as an attribute on the primary model instance

### Example: Extending a User Model

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

### Accessing Data

```python
# Create a user
user = User.objects.create(username="john_doe")

# Create a profile
profile = Profile.objects.create(user=user, bio="Software Engineer")

# Accessing related data
print(user.profile.bio)  # Accessing Profile from User
print(profile.user.username)  # Accessing User from Profile
```

---

## Foreign Key Relationships

A foreign key relationship is a many-to-one relationship where each instance of a model is related to one instance of another model.

### Example: Books and Authors

```python
class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### Querying Foreign Key Data

```python
# Fetch the author
author = Author.objects.get(name="John Doe")

book = Book.objects.create(title="Django for Beginners", author=author)
print(book.author.name)  # Accessing author from book

# Reverse access
author = Author.objects.get(name="John Doe")
print([book.title for book in author.book_set.all()])  # Get books written by author

book = author.book_set.get(title="Django for Beginners")
print(book.title)

books = Book.objects.filter(author__name="John Doe", title="Django for Beginners")

# Iterate through books if multiple exist
for book in books:
    print(f"Title: {book.title}, Author: {book.author.name}")

```

Using `related_name`:

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

# Now access books using `author.books.all()` instead of `author.book_set.all()`
```

---

## Many-to-Many Relationships

### Defining a Many-to-Many Relationship

```python
class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
```

### Populating the `Book` Model with Multiple Authors

```python
book = Book.objects.create(title="Introduction to Machine Learning")
author1 = Author.objects.create(name="Andrew Ng")
author2 = Author.objects.create(name="Michael I. Jordan")

book.authors.add(author1, author2)  # Adding multiple authors
```

### Querying Books and Authors

```python
book = Book.objects.get(title="Introduction to Machine Learning")
print([author.name for author in book.authors.all()])  # Get authors

author = Author.objects.get(name="Andrew Ng")
print([book.title for book in author.book_set.all()])  # Get books written by the author
```

Using `related_name`:

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name="books")

# Now access books using `author.books.all()` instead of `author.book_set.all()`
```

---

## Filtering in Django ORM

### Basic Filters

```python
# Exact match
books = Book.objects.filter(title="Django for Beginners")

# Case-insensitive match
books = Book.objects.filter(title__iexact="django for beginners")
```

### Lookup Filters

```python
# Contains
books = Book.objects.filter(title__contains="Django")

# Starts with / Ends with
books = Book.objects.filter(title__startswith="Django")
books = Book.objects.filter(title__endswith="Python")
```

### Range and Comparison Filters

```python
# Greater than, less than, and between
books = Book.objects.filter(id__gt=5)  # ID greater than 5
books = Book.objects.filter(id__lt=10)  # ID less than 10
books = Book.objects.filter(id__range=(5, 10))  # ID between 5 and 10
```

### Date and Time Filters

```python
from datetime import date

books = Book.objects.filter(published_date__year=2023)
books = Book.objects.filter(published_date__gte=date(2022, 1, 1))  # Published after Jan 1, 2022
```

### Null and Boolean Filters

```python
# Find books with no assigned authors
books = Book.objects.filter(authors__isnull=True)
```

### Chaining Filters

```python
books = Book.objects.filter(title__icontains="Python").filter(authors__name="John Doe")
```

### Using `Q` Objects for Complex Queries

```python
from django.db.models import Q

# Find books with title containing 'Python' OR authored by 'John Doe'
books = Book.objects.filter(Q(title__icontains="Python") | Q(authors__name="John Doe"))
```

### Ordering Results

```python
books = Book.objects.all().order_by("title")  # Ascending order
books = Book.objects.all().order_by("-title")  # Descending order
```

### Limiting Query Results

```python
books = Book.objects.all()[:5]  # First 5 books
```

---

## Summary Table

| Relationship Type   | Django Field         | Fields Involved       | Traversal | Reverse Traversal |
|--------------------|----------------------|----------------------|-----------|------------------|
| One-to-One        | `OneToOneField`      | One object to one object | `user.profile` | `profile.user` Django adds a reverse attribute automatically (e.g., user.profile) making it feel natural to taverse back and forth |
| Foreign Key       | `ForeignKey`         | One object to many objects | `book.author` | `author.book_set.all()` (or `author.books.all()` with `related_name`) |
| Many-to-Many      | `ManyToManyField`    | Many objects to many objects | `book.authors.all()` | `author.book_set.all()` (or `author.books.all()` with `related_name`) |

This guide covers defining relationships, querying models, and using filtering methods effectively in Django ORM.

