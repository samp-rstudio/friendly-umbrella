from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='friendlyumbrella',
    version='0.0.1',
    description='A stupid python package for testing installs from github.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Sam Perman',
    author_email='sam@posit.co',
    keywords=['friendlyumbrella'],
    url='https://github.com/samp-rstudio/friendly-umbrella',
    download_url=''
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
