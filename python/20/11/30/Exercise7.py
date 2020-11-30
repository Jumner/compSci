# Conditionals - Exercise #7

def calculate_total_price( price, coupon_code ):
	taxPrice = price+price*0.13
	if coupon_code == "BONUS" or coupon_code == "BONUS40":
		return taxPrice * (1 - 0.4) # Make it clear that it's a 40% discount
	return taxPrice

def cleanPriceCalc(price,coupon):
	taxPrice = price+price*0.13
	couponMult = 0.6 if coupon=="BONUS" or coupon=="BONUS40" else 1 # I love ternary ops
	return taxPrice*couponMult

# Main

# Conditionals - Exercise #7

itemPrice = 239.99 # These could easily be inputs
couponCode = "BONUS40" # You said that you prefer set values instead of inputs so that is why I used them
print(f'An item that costs ${itemPrice:.2f} costs ${calculate_total_price(itemPrice, couponCode):.2f} with coupon code \"{couponCode}\"')
couponCode = "Not a correct code 😿"
print(f'An item that costs ${itemPrice:.2f} costs ${calculate_total_price(itemPrice, couponCode):.2f} with coupon code \"{couponCode}\"')