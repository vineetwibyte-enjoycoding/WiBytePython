print('Welcome to the WiByte Bakery')
print()

menu = ['Milkshake', 'Ice Cream', 'Chocolate', 'Eclairs  ', 'CupCake  ']
price = [99.99, 120.99, 89.99, 37.99, 51.99]

print('ITEM', 'PRICE (INR), excl. Tax', sep='\t\t\t')
for kk in range(len(menu)):
    print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

shopping_cart = [] 
shopping_quant= []
shopping_complete = 0

while shopping_complete==0:

    order = int(input('Enter 1 to 5 to select an item, 6 to proceed to checkout.\n')) 
    
   
    
    if order <= 5:
        # User wants to purchase something.
        print('You selected', menu[order-1])
        quant = int(input('How many units do you wish to purchase?\n'))

        # Add the item to the shopping cart. 
        # List 1: Shopping Cart items
        # List 2: Quantity
        if menu[order-1] in shopping_cart:
            idx = shopping_cart.index(menu[order-1])
            
            shopping_quant[idx]+=quant
        else:
            shopping_cart.append(menu[order-1])        
            shopping_quant.append(quant)        
        
        print('Added to shopping cart:', quant, 'units of', menu[order-1])
    elif order == 6:
        shopping_complete = 1
    else: 
        print("Sorry that was not a valid input.")
        



        
# Show the shopping cart. 

print()
print('Your Shopping Cart:')

# Separate the number. 
# Give title to the shopping cart. 
# Add the price of every item in the shopping cart, and also the total. 
grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

grand_tot = round(grand_tot, 2)
print()
print('Your total order is (INR)', grand_tot)

print()

next_500 = 500*(grand_tot//500+1)
gap_500 = next_500 - grand_tot



print()

print('If you purchase for (INR)', next_500, 'you will get a 10% discount', sep=' ')
discount_wanted = input('Would you like to take this offer? (Y/N)')
add_quant=[]
if discount_wanted == 'Y':
    print('You have the following options\n')
    for kk in range(len(menu)):
        add_quant.append((int(gap_500//price[kk]+1)))
        print(str(kk+1), '. Add', menu[kk], str(add_quant[kk]), 'units')
    
    add_on = int(input('Please indicate your preference\n'))

    if menu[add_on-1] in shopping_cart:
        idx = shopping_cart.index(menu[add_on-1])
        shopping_quant[idx]+=add_quant[add_on-1]
    else:
        shopping_cart.append(menu[add_on-1])        
        shopping_quant.append(add_quant[add_on-1])        

    print('shopping cart updated')
    print('Proceed to checkout')    
else:
    print('Proceed to checkout')

# Give title to the shopping cart. 
# Add the price of every item in the shopping cart, and also the total. 
grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

print()

dct_rate = 10.0;  # discount in percentage. 
tax_rate = 10.0; # Tax in percentage

if discount_wanted == 'Y':
    discount = round(dct_rate/100.0*grand_tot, 2)
else:
    discount = 0.0; 

tax = round(tax_rate/100.0*(grand_tot-discount), 2)

print('Your total order is (INR)', grand_tot)
print('Discount (10%) is (INR)', discount)
print('Your order value, after discount is (INR)', round(grand_tot-discount, 2))
print('Tax (10%) is (INR)', round(tax, 2)); 
print('Total you have to pay (INR) ', round(grand_tot - discount + tax, 2))

print('Thanks')
print('Bye')

# Fix the problem with discount
# Clean up the final bill. 
