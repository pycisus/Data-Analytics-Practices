raw_orders = [
    {"customer": "  MARIA GARCIA ", "email": "Maria.G@Gmail.com ", "order_id": "ORD-501", "total": " $ 120.50 "},
    {"customer": "Carlos Ramos", "email": "CARLOS@OUTLOOK.COM", "order_id": "ORD-502", "total": "CANCELLED"},
    {"customer": "maria garcia", "email": "maria.g@gmail.com", "order_id": "ORD-501", "total": "120.50"}, # Duplicate order_id
    {"customer": "  LUIS ALVAREZ", "email": "luis@tech.io", "order_id": "ORD-503", "total": "45.00"},
]
clean_orders = []
duplicatedemail = set()
duplicatedid = set()
for orders in raw_orders:
    raw_customer = orders["customer"]
    clean_customer = raw_customer.strip().title()
    raw_email = orders["email"]
    clean_email = raw_email.strip().lower()
    raw_orid = orders["order_id"]
    raw_total = orders["total"]

    if raw_orid in duplicatedid:
        continue
    duplicatedid.add(raw_orid)
    if clean_email in duplicatedemail:
        continue
    duplicatedemail.add(clean_email)
    clean_total = raw_total.strip().replace("$", "")
    try:
        clean_total = float(clean_total)
    except:
        clean_total = 0.0
    clean_orders.append({"customer": clean_customer,"email":clean_email,"order_id":raw_orid,"total": clean_total})
print(clean_orders)