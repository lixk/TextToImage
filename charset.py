# this util is used to detect file or string bytes encoding
# author: lixk
# email: 1749498702@qq.com

# info: UTF includes ISO8859-1，GB18030 includes GBK，GBK includes GB2312，GB2312 includes ASCII
CODES = ['UTF-8', 'UTF-16', 'GB18030', 'BIG5']
# UTF-8 BOM prefix
UTF_8_BOM = b'\xef\xbb\xbf'


def detect(s):
    """
    get file encoding or bytes charset
    
    :param s: file path or bytes data
    
    :return: encoding charset
    """

    if type(s) == str:
        with open(s, 'rb') as f:
            data = f.read()
    elif type(s) == bytes:
        data = s
    else:
        raise TypeError('unsupported argument type!')

    # iterator charset
    for code in CODES:
        try:
            data.decode(encoding=code)
            if 'UTF-8' == code and data.startswith(UTF_8_BOM):
                return 'UTF-8-SIG'
            return code
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError('unknown charset!')


if __name__ == '__main__':
    print(detect('abc哈哈'.encode('gbk')))
    # print(detect([]))
    # print(detect('abc'))
