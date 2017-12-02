import os
import subprocess

cmd = './utils/phantomjs.exe ./utils/rasterize.js http://ariya.github.io/svg/tiger.svg tiger.png'
cmd = './utils/phantomjs.exe ./utils/rasterize.js http://127.0.0.1/index main.jpg'

# os.system(cmd)
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)