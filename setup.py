from setuptools import setup, find_packages

with open("library/PYPI-README.md", "r") as file:
  longDescription = file.read()
  file.close()
with open("shD.md", "r") as file:
  shortDescription = file.read()
  file.close()

setup(
  name="curvv",
  version="0.4.25",
  packages=find_packages(),
  install_requires=[
    "bs4",
    "requests",
    "colorama",
    "rich",
    "importlib",
    "argparse",
  ],
  author="Khalid Azmatullah",
  url="https://github.com/Khalid-Azmatullah/curvv",
  classifiers=[
    "Topic :: Desktop Environment",
  ],
  entry_points={
    "console_scripts": [
      "cvv=curvv:runCvvCommands",
    ],
  },
  description=shortDescription,
  long_description=longDescription,
  long_description_content_type="text/markdown"
)
