# Description: QAP 3 - SD 15 - Python
# Author: Logan Firmage
# Date: July 20th, 2025


# Define required libraries.

import datetime

# Define program functions.

def validate_inputs():
    while True:
        first_name = input("Enter Customer First Name (or 'END' to quit): ").strip().title()
        if first_name.upper() == "END":
            return None # This is the signal to break the loop
        if not first_name:
            print("First name is required.")
            continue

        last_name = input("Enter Customer Last Name: ").strip().title()
        if not last_name:
            print("Last name is required.")
            continue

        phone = input("Enter 10-digit Phone Number: ").strip()
        if not phone.isdigit() or len(phone) != 10:
            print("Phone number must be exactly 10 digits. ")
            continue

        plate = input("Enter 6-character Plate Number: ").strip().upper()
        if len(plate) != 6 or not plate.isalnum():
            print("Plate number must be 6 alphanumeric characters.")
            continue

        make = input("Enter Car Make: ").strip().title()
        model = input("Enter Car Model: ").strip().title()

        try:
            year = int(input("Enter Car Year: ").strip())
            price = float(input("Enter Selling Price (max $50,000): ").strip())
            if price > 50000:
                print("Selling price must not exceed $50,000.")
                continue
            trade_in = float(input("Enter Trade-in Amount: ").strip())
            if trade_in > price:
                print("Trade-in amount cannot exceed selling price.")
                continue
        except ValueError:
            print("Year, price, and trade-in must be numeric.")
            continue

        salesperson = input("Enter Salesperson Name: ").strip().title()
        if not salesperson:
            print("Salesperson name is required.")
            continue

        return {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "plate": plate,
            "make": make,
            "model": model,
            "year": year,
            "price": price,
            "trade_in": trade_in,
            "salesperson": salesperson,
        }
    
def calculate_fees(price, trade_in):
    price_after_trade = price - trade_in
    license_fee = 75.00 if price > 15000 else 0.00
    transfer_fee = price * 0.01
    if price > 20000:
        transfer_fee += price * 0.16 # This is the luxury tax
    subtotal = price_after_trade + license_fee + transfer_fee
    hst = subtotal * 0.15
    total_price = subtotal + hst

    return {
        "price_after_trade": price_after_trade,
        "license_fee": license_fee,
        "transfer_fee": transfer_fee,
        "subtotal": subtotal,
        "hst": hst,
        "total_price": total_price
    }

def generate_receipt_id(first_name, last_name, plate, phone):
    initials = first_name[0].upper() + last_name[0].upper()
    middle = plate[-3:]
    end = phone[-4:]
    return f"{initials}-{middle}-{end}"

def format_phone(phone):
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

def payment_schedule(total_price):
    today = datetime.date.today()
    first_payment_date = datetime.date(today.year, today.month, 1)
    if today.day >= 25:
        first_payment_date += datetime.timedelta(days=32)
    else:
        first_payment_date += datetime.timedelta(days=1)
    first_payment_date = first_payment_date.replace(day=1)

    print("\nPayment Schedule (1 to 4 Years):")
    for years in range (1, 5):
        months = years * 12
        finance_fee = 39.99 * years
        final_price = total_price + finance_fee
        monthly_payment = final_price / months
        print(f"\n{years} Year Plan: ")
        print(f"   Monthly Payments: {months}")
        print(f"   Financing Fee: ${finance_fee:,.2f}")
        print(f"   Total Price: ${final_price:,.2f}")
        print(f"   Monthly Payment: ${monthly_payment:,.2f}")
        print(f".  First Payment Date: {first_payment_date.strftime('%m, %d, %y')}")

# Main program starts here.
while True:
    customer_data = validate_inputs()
    if customer_data is None:
        print("Exiting program.")
        break

    invoice_date = datetime.date.today().strftime("%m, %d, %y")
    full_name = f"{customer_data['first_name'][0]}. {customer_data['last_name']}"
    formatted_phone = format_phone(customer_data['phone'])
    car_details = f"{customer_data['year']} {customer_data['make']} {customer_data['model']}"
    receipt_id = generate_receipt_id(customer_data['first_name'], customer_data['last_name']), 
    customer_data['plate'], customer_data['phone']

    fees = calculate_fees(customer_data['price'], customer_data['trade_in'])

    print(f"Honest Harry's Car Sales")
    print(f"Invoice Date: {invoice_date}")
    print(f"Receipt ID: {receipt_id}")
    print()
    print(f"Selling Price:     ${customer_data['price']:,.2f}")
    print(f"Customer:     {full_name}")
    print(f"Phone:        {formatted_phone}")
    print(f"Car:          {car_details}")
    print(f"Plate #:      {customer_data['plate']}")
    print(f"Salesperson:  {customer_data['salesperson']}")
    print("--------------------------------------------")
    print(f"Selling Price:     ${customer_data['price']:,.2f}")
    print(f"Trade-in:          -${customer_data['trade_in']:,.2f}")
    print(f"Price after Trade: ${fees['price_after_trade']:,.2f}")
    print(f"License Fee:       ${fees['license_fee']:,.2f}")
    print(f"Transfer Fee:      ${fees['transfer_fee']:,.2f}")
    print(f"Subtotal:          ${fees['subtotal']:,.2f}")
    print(f"HST (15%):         ${fees['hst']:,.2f}")
    print(f"Total Sale Price:  ${fees['total_price']:,.2f}")
    print()

    payment_schedule(fees['total_price'])
    print()

        

