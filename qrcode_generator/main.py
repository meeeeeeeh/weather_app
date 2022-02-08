import qrcode


def get_qrcode(url, name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created. Open {name}.png'


def main():
    link = input('enter your url:\n')
    print(get_qrcode(url=link))


if __name__ == '__main__':
    main()
