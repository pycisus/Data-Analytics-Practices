raw_leads = [
    {"name": "  JOHN DOE ", "email": "John.Doe@Gmail.com ", "phone": "+1 (555) 019-2834", "spend": "150.50"},
    {"name": "jane smith", "email": "JANE.SMITH@YAHOO.COM", "phone": "5550192835", "spend": "INVALID"},
    {"name": "John Doe", "email": "john.doe@gmail.com", "phone": "555-019-2834", "spend": "150.50"}, # Duplicate email
    {"name": "  ALICE WILLIAMS", "email": "alice@company.io", "phone": "N/A", "spend": "300.00"},
]
cleaned_email = set()
clean_leads = []
for leads in raw_leads:
    email = leads["email"]
    raw_names = leads["name"]
    raw_phone = leads["phone"]
    raw_spend = leads["spend"]
#cleaned email
    clean_email = email.lower().strip()
    if clean_email in cleaned_email:
        continue
    cleaned_email.add(clean_email)
#cleaned name
    clean_name = raw_names.strip().title()
#clean phones
    digits = ""
    for clean_phones in raw_phone:
        if clean_phones.isdigit():
            digits = digits + clean_phones
    if len(digits) >= 10:
        clean_phones = digits
    else:
        clean_phones = "UNKNOWN"

    try:
        cleand_spend = float(raw_spend)
    except:
        cleand_spend = 0.0
    clean_leads.append({"name" : clean_name,"email": clean_email,"phone": clean_phones,"spend":cleand_spend})
print(clean_leads)