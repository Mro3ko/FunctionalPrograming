transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]

transactions_in_pln = list(map(lambda x: round(x * 4.5,2), transactions_in_eur))


print("Transactions in PLN:")
for amount in transactions_in_pln:
    print(f"{amount}")
