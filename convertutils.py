import subprocess


def render(url, filename, size='', zoom=''):
    """
    render html page to image or pdf file
    :param url: html page addr
    :param filename: generate file name
    :param size: image size or pdf file format
    :param zoom: 
    :return: 
    """
    cmd = './lib/phantomjs.exe ./lib/rasterize.js {} {} {} {}'.format(url, filename, size, zoom)
    print(cmd.encode('utf-8'))
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    result = p.communicate()
    return result[0].decode('utf-8')


if __name__ == '__main__':
    print(render('http://m.baidu.com', 'a.pdf', 'Letter'))
