# Django Model Errors and Debugging Guide

## 1. Model-Specific Errors in Django

### (a) `DoesNotExist`
**Cause:** Trying to retrieve an object that does not exist.

**Example:**
```python
from grocery_store.models import Product

try:
    product = Product.objects.get(pk=1)
except Product.DoesNotExist:
    print("Product not found!")
```
**Fix:** Use `.filter().first()` instead of `.get()`.
```python
product = Product.objects.filter(pk=1).first()
```

---

### (b) `MultipleObjectsReturned`
**Cause:** `.get()` returns multiple objects instead of one.

**Example:**
```python
try:
    product = Product.objects.get(name="Coca-Cola")
except Product.MultipleObjectsReturned:
    print("Multiple products found!")
```
**Fix:** Use `.filter().first()`.
```python
product = Product.objects.filter(name="Coca-Cola").first()
```

---

### (c) `IntegrityError`
**Cause:** Database constraint violation (e.g., unique, foreign key, NOT NULL).

**Example:** Unique constraint violation
```python
from django.db import IntegrityError

try:
    Product.objects.create(name="Coca-Cola")
    Product.objects.create(name="Coca-Cola")  # Duplicate
except IntegrityError:
    print("Product name must be unique!")
```
**Fix:** Ensure uniqueness before saving.

---

### (d) `ValueError`
**Cause:** Invalid value assigned to a field.

**Example:**
```python
try:
    Product.objects.create(name="Pepsi", price="ten")  # Should be a number
except ValueError:
    print("Invalid data type for price!")
```
**Fix:** Validate input data types before saving.

---

### (e) `FieldError`
**Cause:** Querying a non-existent field.

**Example:**
```python
try:
    Product.objects.filter(cost=10)  # 'cost' is not a valid field
except FieldError:
    print("Invalid field name in query!")
```
**Fix:** Check model fields using:
```python
print(Product._meta.get_fields())
```

---

### (f) `OperationalError`
**Cause:** Database connection issue or missing migrations.

**Example:**
```python
try:
    Product.objects.all()
except OperationalError:
    print("Database error!")
```
**Fix:** Run migrations:
```bash
python manage.py migrate
```

---

### (g) `ValidationError`
**Cause:** Data fails model validation.

**Example:**
```python
from django.core.exceptions import ValidationError

try:
    product = Product(name="Milk", price=-5)
    product.full_clean()
except ValidationError as e:
    print(f"ValidationError: {e}")
```
**Fix:** Use field validators.
```python
from django.core.validators import MinValueValidator

class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
```

---

## 2. General Python Errors in Django Models

### (a) `AttributeError`
**Cause:** Accessing an undefined attribute or method.

**Example:**
```python
product = Product.objects.first()
print(product.cost)  # No 'cost' field
```
**Fix:** Check available fields:
```python
print(product._meta.get_fields())
```

---

### (b) `TypeError`
**Cause:** Passing incorrect argument types.

**Example:**
```python
Product.objects.create(name="Fanta", price="free")  # Price should be a number
```
**Fix:** Ensure proper data types.

---

### (c) `KeyError`
**Cause:** Trying to access a missing key in a dictionary.

**Example:**
```python
data = {"name": "Sprite"}
price = data["price"]  # KeyError
```
**Fix:** Use `.get()` with a default value.
```python
price = data.get("price", 0)
```

---

## 3. Summary Table of Django Model Errors

| **Error Type**              | **Cause** | **Fix** |
|-----------------------------|----------|---------|
| `DoesNotExist` | Object not found | Use `.filter().first()` |
| `MultipleObjectsReturned` | More than one object found | Use `.filter().first()` |
| `IntegrityError` | Unique, ForeignKey, or NOT NULL constraint failure | Ensure valid data |
| `ValueError` | Invalid value assigned to field | Use correct data types |
| `FieldError` | Querying a non-existent field | Check model fields |
| `OperationalError` | Database connection issues | Run `python manage.py migrate` |
| `ValidationError` | Data fails model validation | Use validators |
| `AttributeError` | Accessing undefined field/method | Check field names |
| `TypeError` | Incorrect argument type | Match expected types |
| `KeyError` | Missing key in dictionary | Use `.get()` method |

---

## 4. Debugging Tips
- Use Django shell for testing:
  ```bash
  python manage.py shell
  ```
- Wrap queries in `try-except` blocks.
- Use `print()` or `logging.debug()` to track variable values.
- Check Django logs for errors.

---

### **Need More Help?**
Let me know if you'd like to explore specific errors in more detail! 🚀
