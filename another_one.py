raw_bookings = [
    {"guest": "   JUAN PEREZ ", "email": "Juan.Perez@Gmail.com ", "booking_id": "BK-101", "phone": "+52 (782) 555-0101", "deposit": " $ 50.00 "},
    {"guest": "sofia martinez", "email": "SOFIA.M@HOTMAIL.COM", "booking_id": "BK-102", "phone": "7825550102", "deposit": "PENDING"},
    {"guest": "Juan Perez", "email": "juan.perez@gmail.com", "booking_id": "BK-101", "phone": "52-782-555-0101", "deposit": "50.00"}, # Duplicate booking_id
    {"guest": "  MARCO SANCHEZ", "email": "marco@work.com", "booking_id": "BK-103", "phone": "N/A", "deposit": "120.75"},
]
cleaned_bookings = []
duplicated_bookingid = set()
for book in raw_bookings:
    raw_guest = book["guest"]
    clean_guest = raw_guest.strip().title()
    raw_email = book["email"]
    clean_email = raw_email.strip().lower()
    raw_bookinid = book["booking_id"]
    raw_phone = book["phone"]
    raw_deposit = book["deposit"]
    clean_deposit = raw_deposit.replace("$","")
    if raw_bookinid in duplicated_bookingid:
        continue
    duplicated_bookingid.add(raw_bookinid)
    digitonly = ""
    for phone in raw_phone:
        if phone.isdigit():
            digitonly = digitonly + phone
    if len(digitonly) >= 10:
        clean_phone = digitonly
    else:
        clean_phone = "UNKNOWN"
    try:
        clean_deposit = float(clean_deposit)
    except:
        clean_deposit = 0.0
    cleaned_bookings.append({"guest": clean_guest,"email": clean_email,"booking_id": raw_bookinid,"phone": clean_phone, "deposit": clean_deposit})
print(cleaned_bookings)