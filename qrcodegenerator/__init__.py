import qrcode

def create_qr_code_image(data: str):
    """this will generate a qr code hopefully"""

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill='black', back_color='white')