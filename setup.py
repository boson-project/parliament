from setuptools import setup
import pathlib
import os


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(package_root, "parliament", "version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

setup(
    name='parliament-functions',
    packages=['parliament'],
    version=version,
    license='MIT',
    description='A framework for invoking functions over HTTP',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Lance Ball',
    author_email='lball@redhat.com',
    url='https://github.com/boson-project/parliament',
    keywords=['faas', 'functions', 'openshift'],

    install_requires=['cloudevents', 'flask', 'waitress'],

    classifiers=[],
    entry_points={
      "console_scripts": [
        "parliament=parliament.__main__:main",
      ]
    },
)
