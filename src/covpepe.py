import argparse
import base64
import io
import os
import pathlib
import tarfile

import pyperclip


parser = argparse.ArgumentParser(description='Copy files/folders as text, using characters that are safe to share across platforms, or via email / word processors.')
parser.add_argument('PATH', nargs='+', help='Files/folders to copy.')
args = parser.parse_args()

abs_paths = [pathlib.Path(x).absolute() for x in args.PATH]
root_path = os.path.commonpath(abs_paths)
try:
    os.chdir(root_path)
except NotADirectoryError:
    root_path = pathlib.PurePath(root_path).parent
    os.chdir(root_path)

with io.BytesIO() as stream:

    with tarfile.open(mode='w:xz', fileobj=stream) as tar:
        for abs_path in abs_paths:
            path = abs_path.relative_to(root_path)
            tar.add(path)

    raw_data = stream.getvalue()

encoded = base64.b85encode(raw_data)

pyperclip.copy(str(encoded, 'ascii'))
