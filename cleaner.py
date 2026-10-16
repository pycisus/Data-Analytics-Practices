raw_inventory = [
    {"item": "  LAPTOP PRO ", "supplier": "Tech.Global@Corp.com ", "product_id": "PRD-901", "phone": "+52 (782) 111-2233", "unit_price": " $ 1200.50 "},
    {"item": "wireless mouse", "supplier": "PARTS.INC@GMAIL.COM", "product_id": "PRD-902", "phone": "7821112234", "unit_price": "OUT_OF_STOCK"},
    {"item": "Laptop Pro", "supplier": "tech.global@corp.com", "product_id": "PRD-901", "phone": "52-782-111-2233", "unit_price": "1200.50"}, # Duplicate product_id
    {"item": "  MECHANICAL KEYBOARD", "supplier": "keys@dev.net", "product_id": "PRD-903", "phone": "N/A", "unit_price": "85.00"},
]
#Deduplicate by product_id: Use a set() to track seen IDs and skip any duplicate rows using continue.
cleaned_inventory = []
duplicated_product_id = set()
for inventory in raw_inventory:
    raw_product_id = inventory["product_id"]
    if raw_product_id in duplicated_product_id:
        continue
    duplicated_product_id.add(raw_product_id)
    #Clean item: Strip outer spaces and format to Title Case ("Laptop Pro").
    raw_item = inventory["item"]
    clean_item = raw_item.strip().title()
    #Clean supplier: Strip outer spaces and convert to lowercase ("tech.global@corp.com").
    raw_supplier = inventory["supplier"]
    clean_supplier = raw_supplier.strip().lower()
    #Clean phone: Extract digits using a character loop. If len(digits) >= 10, save the digits string; otherwise, set to "UNKNOWN".
    digits = ""
    for phones in inventory["phone"]:
        if phones.isdigit():
            digits = digits + phones
    if len(digits) >= 10:
        clean_phone = digits
    else:
        clean_phone = "UNKNOWN"
    #Clean unit_price: Remove "$" and spaces, then cast to float using a 
    # try / except block (reassigning the variable: unit_price = float(...)). 
    # If conversion fails (e.g., "OUT_OF_STOCK"), set unit_price = 0.0.
    raw_price = inventory["unit_price"]
    clean_price = raw_price.replace("$","").strip()
    try:
        clean_price = float(clean_price)
    except:
        clean_price = 0.0
    cleaned_inventory.append({"item":clean_item,"supplier": clean_supplier,"product_id":raw_product_id,"phone": clean_phone,"unit_price": clean_price})
print(cleaned_inventory)