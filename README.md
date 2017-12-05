# TextToImage
## [en]

This program uses the Python language development, relying on the [PhantomJS](http://phantomjs.org/) library, you can convert text file content to png / jpg format images, or PDF files. Input text support plain text and rich text, you can specify the output file width, height, font, background, zoom factor and so on.

In the `config.ini` file can do the corresponding configuration:

    [input]
    # input file folder
    folder=input
    # declare whether input file data is rich text
    is_richtext=False

    [output]
    # output file folder
    folder=output
    # output file type(png/jpg or pdf)
    file.type=png
    # output image or pdf size
    # paper (pdf output) examples: "5in*7.5in", "10cm*20cm", "A4", "Letter"
    # image (png/jpg output) examples: "1920px" entire page, window width 1920px;"800px*600px" window, clipped to 800x600
    file.size=800px
    # page zoom factor
    file.zoom=1
    # page style(same as html style)
    file.style=background:#fff;color:#000

### Instructions:
Put the text file to be converted into the input folder (default `input` folder) and run `main.py`. After a while,  you can see the output images or PDF files in the output folder.

### Note:
On Windows system, you can run compiled executable file (TextToImage.exe) in the build-exe folder as you do not need to install the Python environment;
For Other operating systems, please replace the phantomjs.exe( in the `lib` folder) with right version, and then run `main.py`. Enjoy it!

---


## [中文]
本程序使用Python语言开发，依赖于 [PhantomJS](http://phantomjs.org/)库，可以将文本文件内容转换为png/jpg格式的图片，或者PDF文件。输入文本支持普通文本和富文本，可以指定输出文件的宽，高，字体，背景，缩放系数等。

可以在`config.ini`文件中做对应配置：

    [input]
    # 要转换的输入文本所在的文件夹
    folder=input
    # 声明是否是富文本
    is_richtext=False

    [output]
    # 输出文件夹
    folder=output
    # 输出文件类型(png/jpg or pdf)
    file.type=png
    # 输出文件尺寸
    # PDF 示例: "5in*7.5in", "10cm*20cm", "A4", "Letter"
    # png/jpg 示例: "1920px"->图片宽度1920px;"800px*600px"->图片裁切到800px*600px
    file.size=800px
    # 页面缩放系数
    file.zoom=1
    # 页面样式(与html样式使用方式相同，可以指定背景色，字体颜色，大小……)
    file.style=background:#fff;color:#000

### 使用方法：
将待转换的文本文件放入输入文件夹（默认`input`文件夹），运行 `main.py`，等程序运行结束，在输出文件夹（默认output文件夹）中即可看到输出的图片或者PDF文件。
### 注意：
Windows系统下，可以直接运行build-exe文件夹内编译打包好的可执行文件（TextToImage.exe）不需要安装Python环境；
其他操作系统，请替换`lib`文件夹下的phantomjs.exe为对应系统下的phantomjs，然后运行`main.py`即可。