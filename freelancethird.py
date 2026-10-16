# Raw client log stream
raw_log = "  pump_01:45.5:NORMAL , PUMP_02:110.0:OVERHEAT, compressor_01:12.0:NORMAL, PUMP_01:5.0:NORMAL, fan_01:85.2:WARNING "

# Base rates dictionary
rates = {
    "hourly_rate": 35.0,
    "overheat_penalty_pct": 20.0,
    "tax_pct": 16.0
}

client_name = input("Write your name: ")
custom_discount_pct = float(input("Write your custom discount: "))
clean_log = raw_log.upper()
log_entries = clean_log.split(",")
total_hours = 0.0
flagged_count = 0.0
machine_list = []
for entry in log_entries:
    clean_entry = entry.strip()
    machine_name, hours, status = clean_entry.split(":")
    hours = float(hours)
    total_hours += hours
    if status == "OVERHEAT" or status == "WARNING":
        flagged_count += 1
    if machine_name not in machine_list:
        machine_list.append(machine_name)
base_cost = total_hours * rates["hourly_rate"]
if flagged_count > 0.0:
    penalty = base_cost *rates["overheat_penalty_pct"]/100
else:
    penalty = 0.0
base_cost = base_cost + penalty
disccount = base_cost*custom_discount_pct/100
tax =  base_cost-disccount*rates["tax_pct"]/100
total_bill = base_cost-disccount+tax

audit_summary ={"client":client_name,
                 "unique machines": machine_list,
                "total hours": round(total_hours,1),
                 "flagged entries": int(flagged_count),
                   "subtotal": base_cost,
                     "final total": round(total_bill,2)}
print(audit_summary)