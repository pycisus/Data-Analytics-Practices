raw_members = [
    {"member": "  ALEX RIVERA ", "email": "Alex.R@Gmail.com ", "member_id": "GYM-301", "phone": "+52 (782) 444-9988", "monthly_fee": " $ 45.00 "},
    {"member": "brenda gomez", "email": "BRENDA.G@YAHOO.COM", "member_id": "GYM-302", "phone": "7824449989", "monthly_fee": "EXPIRED"},
    {"member": "Alex Rivera", "email": "alex.r@gmail.com", "member_id": "GYM-301", "phone": "52-782-444-9988", "monthly_fee": "45.00"}, # Duplicate member_id
    {"member": "  CARLOS MENDOZA", "email": "carlos@dev.io", "member_id": "GYM-303", "phone": "N/A", "monthly_fee": "60.00"},
]
#Deduplicate by member_id: Track seen IDs using a set(). Skip any duplicate rows.
duplicated_memberid = set()
clean_members = []

for id in raw_members:
    cleanid = id["member_id"]
    
    if cleanid in duplicated_memberid:
        continue
    duplicated_memberid.add(cleanid)
    #Clean member: Strip outer spaces and format to Title Case ("Alex Rivera").
    raw_member = id["member"]
    clean_member = raw_member.strip().title()
    #Clean email: Strip outer spaces and convert to lowercase ("alex.r@gmail.com")
    raw_email = id["email"]
    clean_email = raw_email.strip().lower()
    #Clean phone: Use a nested for loop with .isdigit() to extract numeric digits. 
    #If len(digits) >= 10, keep the digits string; otherwise, set to "UNKNOWN".
    raw_phone = id["phone"]
    digits = ""
    for clean_phone in raw_phone:
        if clean_phone.isdigit():
            digits =  digits + clean_phone
    if len(digits) >= 10:
        clean_phone = digits
    else:
        clean_phone = "UNKNOWN"
    #Clean monthly_fee: Remove "$" and spaces, then use try / except to convert to float (reassigning the variable: monthly_fee = float(...)). 
    # If conversion fails (e.g., "EXPIRED"), set monthly_fee = 0.0.
    raw_monthly_fee = id["monthly_fee"]
    clean_monthly_fee = raw_monthly_fee.replace("$","").strip()
    try:
        monthly_fee = float(clean_monthly_fee)
    except:
        monthly_fee = 0.0
    clean_members.append({
        "member":clean_member, 
        "email":clean_email,
        "member_id": cleanid,
        "phone":clean_phone,
        "monthly_fee":monthly_fee})
print(clean_members)