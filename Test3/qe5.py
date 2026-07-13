book_prices=[1000,2000,3000,4000]
new_price=int(input("Enter the new price : "))
book_prices.append(new_price)
for i in range(1, len(book_prices)):
    key = book_prices[i]
    j = i - 1
    while j >= 0 and book_prices[j] > key:
        book_prices[j + 1] = book_prices[j]
        j -= 1
    book_prices[j + 1] = key
print("Updated Price List:", book_prices)