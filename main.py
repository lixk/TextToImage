import glob
import os
from configparser import ConfigParser

import charset
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
file_style = config.get("output", "file.style", fallback='background: #fff')
temp_folder = 'temp'
if not os.path.exists(temp_folder): os.makedirs(temp_folder, exist_ok=True)
temp_file = temp_folder + '/temp.html'

special_chars = {'<': '&lt;',
                 '>': '&gt;',
                 '\n': '<br>',
                 '\t': '&nbsp;&nbsp;',
                 ' ': '&nbsp;',
                 '&': '&amp;',
                 '\'': '&apos;',
                 '"': '&quot;'}

# html template
html = '''
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="{0}">
{1}
</body>
</html>
'''


def convert_file():
    """
    convert file to images or PDF files
    
    :return: 
    """
    files = glob.glob('{0}/*'.format(data_in))
    for file in files:
        basename = os.path.basename(file)
        output_file = os.path.join(data_out, '{0}.{1}'.format(os.path.splitext(basename)[0], file_type))

        # read input file data
        with open(file, 'r', encoding=charset.detect(file)) as src:
            text = src.read()
            # if the file is empty, skip it
            if not text:
                continue
            if 'false' == is_richtext.lower():
                # replace special character
                text = ''.join(map(lambda char: special_chars.get(char, char), text))
                # write text to the temp file
            with open(temp_file, 'w', encoding='utf-8') as temp:
                temp.write(html.format(file_style, text))

        # render the temp file to image or pdf
        result = render(temp_file, output_file, file_size, file_zoom)
        print('complete:', output_file, result)


def convert_webpage(url, file_basename):
    """
    convert web page to images or PDF files
     
    :param url: web page url, example: 'http://www.baidu.com'
    :param file_basename: output file basename, example: 'baidu'
    :return: 
    """
    filename = os.path.join(data_out, '{0}.{1}'.format(file_basename, file_type))
    result = render(url, filename, file_size, file_zoom)
    print('complete:', filename, result)


if __name__ == '__main__':
    print('convert start...')
    convert_file()
    # convert_webpage('http://www.baidu.com', 'baidu')
    input('convert complete!\npress enter key to exit...')
