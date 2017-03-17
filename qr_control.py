# external libraries
import pyqrcode


def image(string, path):
    url = pyqrcode.create(string)
    url.svg(path, scale=8)


if __name__ == '__main__':
    image("https://pypi.python.org/pypi/qrcode")
