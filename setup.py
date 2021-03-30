from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='parliament-functions',
    packages=['parliament'],
    version='0.0.4',
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
