import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pip-package-demo', ##name of repo enclosing folder (pip-package-demo)
    version='0.0.1',
    author='Sandeep Junnarkar', ## your name
    author_email='sjnews@gmail.com', ## your email
    description='Math functions i use a lot', ## description of package
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sandeepmj/testFunc',# url to repo
    project_urls = {
        "Bug Tracker": "https://github.com/sandeepmj/testFunc/issues"
    }, ## url to issues page on your repo
    license='MIT',
    packages=['mathFunctions'], ## name of folder that holds the functions
    install_requires=[], ## names of packages required to run your functions
)