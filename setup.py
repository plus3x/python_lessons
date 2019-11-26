from setuptools import setup, find_packages

setup(
  name='python_lessons',
  description='Python lessons',
  version='0.0.1',
  url='https://github.com/plus3x/python_lessons.git',
  author='Vladislav Petrov',
  author_email='electronicchest@gmail.com',
  packages=find_packages(),
  install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
