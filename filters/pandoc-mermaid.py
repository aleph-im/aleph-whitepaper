#!/usr/bin/env python3

import os
import sys
import subprocess

from pandocfilters import toJSONFilter, Para, Image
from pandocfilters import get_filename4code, get_caption, get_extension

# Environment variables with fallback values
MERMAID_BIN = os.environ.get('MERMAID_BIN', 'node_modules/.bin/mmdc')
PUPPETEER_CFG = os.environ.get('PUPPETEER_CFG', None)

def mermaid(key, value, format_, _):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value

        if "mermaid" in classes:
            caption, typef, keyvals = get_caption(keyvals)

            filename = get_filename4code("mermaid", code)
            filetype = get_extension(format_, "png", html="svg", latex="pdf")

            src = filename + '.mmd'
            dest = filename + '.' + filetype

            if not os.path.isfile(dest):
                txt = code.encode(sys.getfilesystemencoding())
                with open(src, "wb") as f:
                    f.write(txt)

                # Default command to execute
                cmd = [MERMAID_BIN, "-i", src, "-o", dest]

                cmd.extend(["-c", "filters/mermaid.json"])
                cmd.extend(["-C", "filters/mermaid.css"])
                cmd.extend(["-b", "transparent"])

                if PUPPETEER_CFG is not None:
                    cmd.extend(["-p", PUPPETEER_CFG])

                if os.path.isfile('.puppeteer.json'):
                    cmd.extend(["-p", ".puppeteer.json"])

                subprocess.check_call(cmd)
                sys.stderr.write('Created image ' + dest + '\n')
		
                if filetype == 'pdf':
                    # Default command to execute
                    cmd = ['pdfcrop', dest, dest]

                    subprocess.check_call(cmd)
                    sys.stderr.write('Cropped image ' + dest + '\n')

            return Para([Image([ident, [], keyvals], caption, [dest, typef])])


def main():
    toJSONFilter(mermaid)


if __name__ == "__main__":
    main()

