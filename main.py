import requests

while True:
    try:
        amount=float(input("enter a amount: "))
        if amount<0:
            print("your amount should be numeric and positive")
            continue
        break
    except ValueError:
        print("please enter valid number")
while True:
    current_currency=input("enter your current currency:").strip().upper()
    if len(current_currency)==3 and current_currency.isalpha():
        break
    print("enter a correct currency")

while True:
    target_currency=input("enter a currency that you need to convert:").strip().upper()
    if len(target_currency)==3 and target_currency.isalpha():
        break
    print("enter a corrent currency")

print("\nInput received successfully\n")
print("Amount: ",amount)
print("From: ",current_currency)
print("To: ",target_currency)


API_KEY="b9198b3d85011219c190848b"

url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{current_currency}"

try:
    response=requests.get(url)
    data = response.json()
except Exception as e:
    print("Error while requesting data:", e)
    exit()

# Check if API returned success
if data.get("result") != "success":
    print("API error:", data.get("error-type"))
    exit()
# Try to get the rate for the target currency
conversion_rates = data.get("conversion_rates", {})
rate = conversion_rates.get(target_currency)

if rate is None:
    print("The currency code", target_currency, "is not valid or not supported.")
    exit()

print("Rate fetched successfully:", rate)

# Conversion 
converted_amount = amount * rate
print("\nConversion Result")
print(f"{amount} {current_currency} = {converted_amount:.2f} {target_currency}")