import bottle
from bottle import request
app = bottle.Bottle
from convertutils import render

html = '''
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
{0}
</body>
</html>
'''
text = ''


@app.route('/index')
def index():
    return html.format(text)


@app.route('/convert', method=['GET', 'POST'])
def convert():
    global text
    text = request.params.get('text', '')
    filename = request.params.get('filename', '')
    size = request.params.get('size', '')
    zoom = request.params.get('zoom', '')

    render('http://127.0.0.1:9999/index', filename, size, zoom)
    with open('test.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)
    return data.format(s)


app.run(host='0.0.0.0', port=80)
