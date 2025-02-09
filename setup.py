from setuptools import setup

# read the contents of your README file
from os import path

THISDIRECTORY = path.abspath(path.dirname(__file__))
with open(path.join(THISDIRECTORY, "README.md")) as f:
    LONGDESC = f.read()

setup(
    name="tehran-stocks",
    version="0.5.4",
    description="DataDownloader for Tehran stock market",
    url="http://github.com/ghodsizadeh/tehran-stocks",
    author="Mehdi Ghodsizadeh",
    author_email="mehdi.ghodsizadeh@gmail.com",
    license="MIT",
    long_description=LONGDESC,
    long_description_content_type="text/markdown",
    packages=["tehran_stocks"],
    install_requires=["pandas", "sqlalchemy"],
    zip_safe=False,
    python_requires=">=3.6",
    scripts=["bin/ts-get"],
)
