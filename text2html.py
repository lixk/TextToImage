import bottle

app = bottle.Bottle()

data = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
{0}
</body>
</html>
'''


@app.route('/index')
def index():
    with open('test.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)
    return data.format(s)


app.run(host='0.0.0.0', port=80)
