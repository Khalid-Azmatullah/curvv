from setuptools import setup, find_packages

with open("README.md", "r") as file:
  longDescription = file.read()
  file.close()
with open("shD.md", "r") as file:
  shortDescription = file.read()
  file.close()

setup(
  name="curvv",
  version="0.4.20",
  packages=find_packages(),
  install_requires=[
    "bs4",
    "requests",
    "colorama",
    "rich",
    "importlib",
    "argparse",
  ],
  entry_points={
    'console_scripts': [
      'cvv=curvv:runCvvCommands',
    ],
  },
  description=shortDescription,
  long_description=longDescription,
  long_description_content_type="text/markdown"
)
