import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_receipt(receipt_number, customer_name, items, total_amount, payment_method):
    # Get desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = os.path.join(desktop_path, f"Payment_Receipt_{receipt_number}.pdf")

    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Payment Receipt")

    # Receipt Details
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Receipt No: {receipt_number}")
    c.drawString(50, height - 100, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, height - 120, f"Customer Name: {customer_name}")

    # Items Table
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, "Item")
    c.drawString(250, height - 160, "Price")

    c.setFont("Helvetica", 12)
    y_position = height - 180
    for item, price in items.items():
        c.drawString(50, y_position, item)
        c.drawString(250, y_position, f"${price:.2f}")
        y_position -= 20

    # Total Amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_position - 20, f"Total Amount: ${total_amount:.2f}")
    c.drawString(50, y_position - 40, f"Payment Method: {payment_method}")

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(50, y_position - 80, "Thank you for your purchase!")

    c.save()
    print(f"Receipt saved as {file_name}")

# Example Usage:
items_purchased = {"Product A": 50.00, "Product B": 30.00, "Service C": 20.00}
generate_receipt(receipt_number="123456",
                 customer_name="John Doe",
                 items=items_purchased,
                 total_amount=100.00,
                 payment_method="Credit Card")
