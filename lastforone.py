raw_students = [
    {"name": "  VALERIA RIOS ", "email": "Val.Rios@Edu.net ", "student_id": "STD-501", "phone": "+52 (782) 555-0199", "tuition_paid": " $ 350.00 "},
    {"name": "carlos santana", "email": "CARLOS.S@GMAIL.COM", "student_id": "STD-502", "phone": "7825550198", "tuition_paid": "PENDING"},
    {"name": "Valeria Rios", "email": "val.rios@edu.net", "student_id": "STD-501", "phone": "52-782-555-0199", "tuition_paid": "350.00"}, # Duplicate student_id
    {"name": "  MARIA FERNANDA", "email": "mafe@tech.io", "student_id": "STD-503", "phone": "N/A", "tuition_paid": "400.00"},
]
duplicated_stid = set()
emptyclean_students = []
#Deduplicate by student_id: Use a set() to track seen IDs and skip any duplicates using continue.
for students in raw_students:
    raw_id = students["student_id"]
    if raw_id in duplicated_stid:
        continue
    duplicated_stid.add(raw_id)
    #Clean name: Strip outer spaces and format to Title Case ("Valeria Rios").
    raw_names = students["name"]
    clean_name = raw_names.strip().title()
    #Clean email: Strip outer spaces and convert to lowercase ("val.rios@edu.net").
    raw_email = students["email"]
    clean_email = raw_email.strip().lower()
    #Clean phone: Extract digits using a character loop. If len(digits) >= 10, keep the digits string; otherwise, set to "UNKNOWN".
    raw_phone = students["phone"]
    digits = ""
    for char in raw_phone:
        if char.isdigit():
            digits = digits + char
    if len(digits) >= 10:
        clean_phone = digits
    else:
        clean_phone = "UNKNOWN"
    #Clean tuition_paid: Remove "$" and spaces, 
    # then cast to float using a try / except block (reassigning the variable: tuition_paid = float(...)). 
    # If conversion fails (e.g., "PENDING"), set tuition_paid = 0.0.
    raw_tuition = students["tuition_paid"]
    clean_tuition_paid = raw_tuition.replace("$","").strip()
    try:
        clean_tuition = float(clean_tuition_paid)
    except:
        clean_tuition = 0.0
    emptyclean_students.append({"name":clean_name,"email":clean_email,"student_id":raw_id,"phone":clean_phone,"tuition_paid":clean_tuition})
print(emptyclean_students)