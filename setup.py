from setuptools import setup as setup_tools
from setuptools import find_packages as fnd_pkg


long_description = '''# HTML Python
Run python commands from html file (on server as Flask)
# Flask Example
```
import htmlpy
htmlpy.set_templates_dir('templates')
# Some code here -_-
@app.route('/')
def index():
    return htmlpy.render('index.html')
```
index.html :
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  {{ About }}<br>
  <htmlpy>
    print(exec('python test.py arg1 arg2'))
  </htmlpy>
</body>

</html>
```
'''

setup_tools(
    name="ps_htmlpy",
    version="0.0.3",
    author="Pixelsuft",
    description="Run python commands from html file (on server as Flask)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pixelsuft/htmlpy/",
    packages=fnd_pkg(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.5',
    license='MIT',
    keywords='htmlpy',
    install_requires=[''],
    py_modules=["htmlpy"]
)
