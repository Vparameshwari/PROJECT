import qrcode

# Create QR object
qr = qrcode.QRCode()

# UPI details
upi_id = "alwinabrisha@okhdfcbank"
name = "Alwinabrisha"
note = "have fun"
amount = "1"

# UPI payment link
link = f"upi://pay?pa={upi_id}&pn={name}&tn={note}&am={amount}&cu=INR"

# Add data to QR
qr.add_data(link)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR image
img.save("gpay_qr.png")

print("QR Code Created Successfully!")
