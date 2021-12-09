import qrcode
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=10,
)
qr.add_data('Some datj')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("some_file1.png")