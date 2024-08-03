import qrcode

def generar_codigo_qr(url, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

if __name__ == "__main__":
    url = "https://iplogger.com/2aidF5"
    nombre_archivo = "codigo_qr_iplogger.png"  # Puedes cambiar el nombre del archivo si lo deseas
    generar_codigo_qr(url, nombre_archivo)
    print(f"Se ha generado el código QR para la URL '{url}' en el archivo: {nombre_archivo}")
