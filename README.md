<h1 align="center">
<img src="library/Curvv..svg" width="300">
</h1><br>

[Curvv](https://pypi.org/project/curvv/) is an open-minded **python package** which focuses on **deployability** of a program on devices which do not have required packages installed along with other functionality.

To install curvv run:
```
pip install curvv
```

## Uses

The best function of curvv is the **packageSafety(_\*args_)**.

For example, suppose you are making a program that requires you to import the [*numpy*](https://pypi.org/project/numpy/) package however you are not sure if the device where the program shall run has [*numpy*](https://pypi.org/project/numpy/)
installed. This is where the **packageSafety(_\*args_)** function becomes useful. 

Just write:
```
import curvv
from curvv import packageSafety as pS

pS("numpy")
```
This shall check if the [*numpy*](https://pypi.org/project/numpy/) package is installed and if it does not find the package it will automatically install the package(s).

![Curvv_logo](https://upload.wikimedia.org/wikipedia/commons/7/70/Docker_logo.png)


Other funx include:
- wait( *\*time* )
- end( *\*time* )
- clearCache()

## Other CLI commands

Curvv has CLI commands for many tasks including creating github repos. 

Simply run the following in the command prompt:
```
cvv gh-new --token {your_github_api} {repository_name} {repository_type}
```

## Last Updated:
```
03/10/2024
```

## Issues
- Run Time
  ![Loading_gif](https://upload.wikimedia.org/wikipedia/commons/a/a5/Barralgoogog.gif)

## Acknowledgements
- [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page)
- [Github Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Pixegami](https://www.youtube.com/watch?v=Kz6IlDCyOUY)