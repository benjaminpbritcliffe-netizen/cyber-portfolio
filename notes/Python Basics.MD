
# 🚗 Python Basics for Car Sales Scenario

A beginner-friendly breakdown of Python fundamentals using a car dealership example.

---

## ✅ Booleans and Boolean Expressions

```python
python
CopyEdit
car_available = True
car_price = 18000
budget = 20000

if car_available and car_price <= budget:
    print("This car is available and within budget!")
else:
    print("This car is either not available or over your budget.")

```

---

## ✅ If-Elif-Else Statements

```python
python
CopyEdit
car_age = 4

if car_age < 1:
    print("Brand new car - no discount.")
elif car_age < 3:
    print("Slightly used - 10% discount.")
elif car_age < 5:
    print("Used car - 20% discount.")
else:
    print("Old model - 30% discount.")

```

---

## ✅ For Loop Example

```python
python
CopyEdit
cars = ["Honda Civic", "Toyota Corolla", "Ford Focus"]

for car in cars:
    print(f"{car} is available for purchase.")

```

---

## ✅ While Loop Example

```python
python
CopyEdit
offer = 15000
min_price = 18000

while offer < min_price:
    print(f"Offer of ${offer} is too low.")
    offer += 1000

print(f"Offer of ${offer} accepted!")

```

---

## ✅ Tuples and Lists

### 🔹 Tuples: Car Specifications

```python
python
CopyEdit
car_specs = ("Honda Civic", 2020, "Automatic")

# Unpacking tuple
model, year, transmission = car_specs
print(f"Model: {model}, Year: {year}, Transmission: {transmission}")

```

---

### 🔹 Lists: Inventory Management

```python
python
CopyEdit
inventory = ["Mazda 3", "Ford Fiesta", "Tesla Model 3"]
inventory.append("BMW 3 Series")
inventory.remove("Ford Fiesta")

print("Updated inventory:", inventory)

```
