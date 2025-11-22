# طباعة معلوماتي
Name = "Raghad Shehada"
Age = 21
Major = "Software Engineering"

print("الاسم:", Name)
print("العمر:", Age)
print("التخصص:", Major)
print()

# مصفوفة منتجات وأسعارها
products = [
    {"name": "Laptop Stand", "price": 25},
    {"name": "USB-C Cable", "price": 8},
    {"name": "Notebook", "price": 3}
]

# foreach في بايثون = for loop على العناصر
for item in products:
    print(f"المنتج: {item['name']} — السعر: {item['price']}$")
