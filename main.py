import glob
import os
from configparser import ConfigParser

from convertutils import render

# read config parameters
config = ConfigParser()
config.read('config.ini')
data_in = config.get("input", "folder", fallback='input')
if not os.path.exists(data_in): os.makedirs(data_in, exist_ok=True)
is_richtext = config.get("input", "is_richtext", fallback='False')
data_out = config.get("output", "folder", fallback='output')
if not os.path.exists(data_out): os.makedirs(data_out, exist_ok=True)
file_type = config.get("output", "file.type", fallback='png')
file_size = config.get("output", "file.size", fallback='')
file_zoom = config.get("output", "file.zoom", fallback='')
file_background_color = config.get("output", "file.background.color", fallback='#fff')
temp_file = 'temp/temp.html'
special_chars = {'<': '&lt;',
                 '>': '&gt;',
                 '\r\n': '<br>',
                 '\n': '<br>',
                 '\t': '&nbsp;&nbsp;',
                 ' ': '&nbsp;',
                 '&': '&amp;',
                 '\'': '&apos;',
                 '"': '&quot;'}

# html template
html = '''
<!DOCTYPE html>
<head><meta charset="UTF-8"></head>
<body style="background: ''' + file_background_color + '''">{0}</body>
</html>
'''


def convert():
    files = glob.glob('{0}/*'.format(data_in))
    for file in files:
        basename = os.path.basename(file)
        output_file = os.path.join(data_out, '{0}.{1}'.format(os.path.splitext(basename)[0], file_type))
        print(output_file)
        # read input file data
        with open(file, 'r', encoding='utf-8') as src:
            text = src.read()
            if 'false' == is_richtext.lower():
                # replace special character
                text = ''.join(map(lambda char: special_chars.get(char, char), text))
                # write text to the temp file
            with open(temp_file, 'w', encoding='utf-8') as temp:
                print(html.format(text).encode())
                temp.write(html.format(text))

        # render the temp file to image or pdf
        render(temp_file, output_file, file_size, file_zoom)


if __name__ == '__main__':
    convert()
