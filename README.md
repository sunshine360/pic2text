# pic2text
use pytessact ocr test
sunshine-图片识别程序
把文华财经的数据读出来写成CSV文件存储然后转为Excel。


项目包含：
1、 基于Tesseract-OCR的图片识别引擎
2、 汉字的识别与处理
3、 数据的整理与存储


安装依赖：
1、 pip install PIL（PILLOW）
2、 Tesseract-OCR以及中文识别库chi_sim.traineddata

使用：
1、双击运行，读取当天的日期下上证的图片进行识别。
2、命令行运行，通过往命令行输入参数进行运行，输入两个参数时，第二个参数当做识别图片信息；输入四个参数时，第三，第四个参数为文件读取路径，文件存储路径。

