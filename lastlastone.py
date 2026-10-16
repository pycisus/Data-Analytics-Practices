raw_loans = [
    {"book_title": "  PYTHON CRASH COURSE ", "email": "User.One@Email.com ", "loan_id": "LBN-101", "phone": "+52 (782) 333-7788", "deposit": " $ 150.00 "},
    {"book_title": "clean code", "email": "DEV.GURU@GMAIL.COM", "loan_id": "LBN-102", "phone": "7823337789", "deposit": "EXPIRED_FEE"},
    {"book_title": "Python Crash Course", "email": "user.one@email.com", "loan_id": "LBN-101", "phone": "52-782-333-7788", "deposit": "150.00"}, # Duplicate loan_id
    {"book_title": "  THE PRAGMATIC PROGRAMMER", "email": "coder@dev.io", "loan_id": "LBN-103", "phone": "N/A", "deposit": "200.00"},
]
#Deduplicate by loan_id: Use a set() to track seen IDs and skip any duplicate rows using continue.
emptycleanloans = []
duplicated_id = set()
for rloans in raw_loans:
    loanid = rloans["loan_id"]
    if loanid in duplicated_id:
        continue
    duplicated_id.add(loanid)
    #Clean book_title: Strip outer spaces and format to Title Case ("Python Crash Course").
    rawbooktitle = rloans["book_title"]
    clean_book_title = rawbooktitle.strip().title()
    #Clean email: Strip outer spaces and convert to lowercase ("user.one@email.com").
    raw_email = rloans["email"]
    clean_email = raw_email.strip().lower()
    #Clean phone: Extract digits using a character loop with .isdigit(). 
    #If len(digits) >= 10, keep the digits string; otherwise, set to "UNKNOWN".
    raw_phone = rloans["phone"]
    digits = ""
    for char in raw_phone:
        if char.isdigit():
            digits = digits + char
    if len(digits) >= 10:
        clean_number = digits
    else:
        clean_number = "UNKNOWN"
    #Clean deposit: Remove "$" and spaces, then cast to float using a try / except block (reassigning the variable: deposit = float(...)). 
    #If conversion fails (e.g., "EXPIRED_FEE"), set deposit = 0.0.
    raw_deposit = rloans["deposit"]
    clean_deposit = raw_deposit.replace("$","").strip()
    try:
        deposit = float(clean_deposit)
    except:
        deposit = 0.0
    emptycleanloans.append({"book_title":clean_book_title,"email":clean_email,"loan_id":loanid,"phone":clean_number,"deposit":deposit})
print(emptycleanloans)