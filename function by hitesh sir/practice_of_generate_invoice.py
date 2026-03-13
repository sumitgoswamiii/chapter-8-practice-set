def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
    total = 0.0
    invoice_line = [f"invoice for {customer_name}: "]
    if items:
        invoice_line.append("Item:")
        for item in items:
            invoice_line.append(f"-{item}")

    if charges:
        invoice_line.append("charges:")
        for label, amount in charges.items():
            invoice_line.append(f"{label.capitalize()}: {amount}")
            total += amount

    invoice_line.append(f"total amount due: {total}")
    return "\\n".join(invoice_line)


            
