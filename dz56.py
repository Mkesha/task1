proceed = int(input("Enter proceed: "))
outlay = int(input("Enter outlay: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"You have {profitability} profitability")
    worker = int(input("How many people work "))
    print(f"{profitability/worker} for one man")
elif proceed == outlay:
    print("No profitability")
else:
    print("lesion")