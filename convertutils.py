# convert text/html to image or pdf util collections
# author: lixk
# email: 1749498702@qq.com

import subprocess


def render(url, filename, size='', zoom=''):
    """
    render html page to image or pdf file
    
    :param url: html page addr
    :param filename: generate file name, suffix (png/jpg or pdf)
    :param size: pdf paper format or image size\n
        paper (pdf output) examples: "5in*7.5in", "10cm*20cm", "A4", "Letter"\n
        image (png/jpg output) examples: "1920px"-> entire page, window width 1920px;
        "800px*600px" -> window clipped to 800px*600px
    :param zoom: zoom factor
    :return: 
    """
    cmd = './lib/phantomjs.exe ./lib/rasterize.js {} {} {} {}'.format(url, filename, size, zoom)
    print(cmd.encode('utf-8'))
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    result = p.communicate()
    return result[0].decode('utf-8')


def text_to_richtext(text):

    pass

if __name__ == '__main__':
    print(render('http://m.baidu.com', 'a.pdf', 'Letter'))
