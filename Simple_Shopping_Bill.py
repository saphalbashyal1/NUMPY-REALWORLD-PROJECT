import numpy as np

items=np.array(["Chicken","Mutton","Soyabean","Egg","Proteinpowdr","Fish"])
prices=np.array([380,1600,200,650,5500,850])
quantities=np.array([1,3,4,1,1,2])

items_total=prices*quantities
total=np.sum(items_total)

discount=np.where(items_total>=500,0.1*items_total,0)
dis=np.sum(discount)
Final_price=items_total-discount
pay=np.sum(Final_price)
print(f"{'ITEMS':12}{'PRICE':>7}{'QTY':>5}{'TOTAL':>7}{'DISC':>6}{'FINAL':>7}")
print("-"*46)

for i in range(len(items)):
    print(f"{items[i]:12} {prices[i]:>7}{quantities[i]:>5}{items_total[i]:>7}{discount[i]:>6} {Final_price[i]:>7}")
print("-"*46)

print(f"Grand_Total : Rs {total}")
print(f"Total Discount : Rs {dis}")
print(f"Amount to pay : Rs {pay}")