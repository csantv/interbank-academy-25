import csv


def main():
    final_amount = 0
    num_debit = 0
    num_credit = 0
    tx_list = []

    with open("data.csv", newline='', encoding="utf-8") as csvfile:
        tx_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        _ = next(tx_reader, None)  # skip header
        for tx_id, tx_type, tx_amount in tx_reader:
            if tx_type == 'Crédito':
                num_credit += 1
                final_amount += float(tx_amount)

            if tx_type == 'Débito':
                num_debit += 1
                final_amount -= float(tx_amount)

            tx_list.append({
                "id": tx_id,
                "amount": float(tx_amount)
            })

    max_tx = max(tx_list, key=lambda x: x['amount'])

    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print("Balance Final:", final_amount)
    print("Transacción de Mayor Monto: ID", max_tx["id"], "-", max_tx["amount"])
    print("Conteo de Transacciones: Crédito:", num_credit, "Débito:", num_debit)


if __name__ == "__main__":
    main()
