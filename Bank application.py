print("===== Welcome to ABC Bank Loan System ======\n")

# .....Basic info of user......
Name = input("Enter your name: ")

Age = int(input("Enter your age: "))

if Age < 21:
    print("\n❌ Loan Rejected: Minimum age should be 21")
    exit()

elif Age <= 45:
    print("\n✅ Age Verified: You meet the age requirement")
        
else:
    print("\n❌ Loan Rejected: Maximum age limit is 45")
    exit()

# .......User categories Select.......
print("\n" + "="*50)
print("Select Loan Categories:")
print("1. Personal Loan (Income: 2-5 Lac)")
print("2. Car Loan (Income: 5-7 Lac)")
print("3. House Loan (Income: 7 Lac+)")
print("="*50)

categories_of_loan = int(input("\nEnter loan category (1/2/3): "))

# -------- Main Loan Selection --------
if categories_of_loan == 1:
    loan_type = "Personal"
    duration_years = 2
    print("\n📋 Personal Loan Options:")
    print("1. 10 Lac")
    print("2. 20 Lac")
    print("3. 40 Lac")

    choice = int(input("Select option (1/2/3): "))
    if choice == 1:
        amount = 1000000
    elif choice == 2:
        amount = 2000000
    elif choice == 3:
        amount = 4000000
    else:
        print("❌ Invalid option")
        exit()

elif categories_of_loan == 2:
    loan_type = "Car"
    duration_years = 3
    print("\n🚗 Car Loan Options:")
    print("1. 30 Lac")
    print("2. 50 Lac")
    print("3. 60 Lac")

    choice = int(input("Select option (1/2/3): "))
    if choice == 1:
        amount = 3000000
    elif choice == 2:
        amount = 5000000
    elif choice == 3:
        amount = 6000000
    else:
        print("❌ Invalid option")
        exit()

elif categories_of_loan == 3:
    loan_type = "House"
    duration_years = 4
    print("\n🏠 House Loan Options:")
    print("1. 70 Lac")
    print("2. 80 Lac")
    print("3. 90 Lac")

    choice = int(input("Select option (1/2/3): "))
    if choice == 1:
        amount = 7000000
    elif choice == 2:
        amount = 8000000
    elif choice == 3:
        amount = 9000000
    else:
        print("❌ Invalid option")
        exit()

else:
    print("❌ Invalid Loan Category")
    exit()

print("\n" + "="*50)
print(f"Selected Loan Type: {loan_type}")
print(f"Loan Amount: Rs. {amount:,}")
print(f"Repayment Duration: {duration_years} years")
print("="*50)

# -------- Income Check --------
monthly_income = int(input("\nEnter your monthly income (PKR): "))

# Income eligibility check based on loan type
if loan_type == "Personal":
    if monthly_income < 200000:
        print("\n❌ Loan Rejected: Personal loan requires minimum 2 Lac monthly income")
        exit()
    elif monthly_income > 500000:
        print("\n💡 Note: With your income, you're also eligible for Car and House loans!")

elif loan_type == "Car":
    if monthly_income < 500000:
        print("\n❌ Loan Rejected: Car loan requires minimum 5 Lac monthly income")
        exit()
    elif monthly_income > 700000:
        print("\n💡 Note: With your income, you're also eligible for House loan!")

elif loan_type == "House":
    if monthly_income < 700000:
        print("\n❌ Loan Rejected: House loan requires minimum 7 Lac monthly income")
        exit()

# -------- Loan Approved - Calculate Monthly Payment --------
print("\n" + "="*50)
print("🎉 LOAN APPROVED! 🎉")
print("="*50)

# Calculate monthly installment (no interest as mentioned)
total_months = duration_years * 12
monthly_payment = amount / total_months

print(f"\n📊 Loan Details for {Name}:")
print(f"   Loan Type: {loan_type} Loan")
print(f"   Total Amount: Rs. {amount:,}")
print(f"   Duration: {duration_years} years ({total_months} months)")
print(f"   Monthly Income: Rs. {monthly_income:,}")
print(f"   Monthly Installment: Rs. {monthly_payment:,.2f}")
print(f"   Interest Rate: 0% (No Interest)")

# Calculate what percentage of income goes to loan
income_percentage = (monthly_payment / monthly_income) * 100
print(f"   % of Income: {income_percentage:.1f}%")

print("\n" + "="*50)
print("Thank you for choosing ABC Bank! 🏦")
print("="*50)