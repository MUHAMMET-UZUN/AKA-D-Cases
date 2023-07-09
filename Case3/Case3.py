import qrcode

def CreateQRCode(content, fileName):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(fileName)


content = input("Type qr code content: ")
fileName = input("File name WITH EXTENSION (example.png): ")

CreateQRCode(content, fileName)
