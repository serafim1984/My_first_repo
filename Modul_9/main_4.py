def discount_price(discount):

    def price_after_discount(price):

        pad = price - price * discount

        return pad

    return price_after_discount

print(discount_price(0.1)(100))