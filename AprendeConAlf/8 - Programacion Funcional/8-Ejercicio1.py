def applyDiscount(price, discount):
    return price - price * (discount / 100)

def applyIVA(price, iva):
    return price + price * (iva / 100)

def priceBasket(basket, function):
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', priceBasket({1000:20, 500:10, 100:1}, applyDiscount))
print('El precio de la compra tras aplicar el IVA es: ', priceBasket({1000:20, 500:10, 100:1}, applyIVA))