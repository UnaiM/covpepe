import argparse
import base64
import io
import tarfile

import pyperclip


parser = argparse.ArgumentParser(description='Convert data in the clipboard, copied using covpepe, to files/folders in the current directory.')
args = parser.parse_args()

encoded = bytes(pyperclip.paste(), 'ascii')

raw_data = base64.b85decode(encoded)

with io.BytesIO() as stream:
    stream.write(raw_data)
    stream.seek(0)

    with tarfile.open(fileobj=stream) as tar:
        try:
            tar.extractall(filter='data')
        except TypeError: # Python 3.11 or lower.
            tar.extractall()
