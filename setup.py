from setuptools import setup, find_packages

setup(name='myapp',
      version='0.1',
      scripts=['run.py'],
      description='My Python Flask Application',
      install_require=['Flask'],
      packages=find_packages(),
      url='https://github.com/avijitpal9/cicd',
      author='AvijitPal',
      zip_safe=False)
