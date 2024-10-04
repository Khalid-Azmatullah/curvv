def importModuleLibrary():
  import requests
  from bs4 import BeautifulSoup as htmlParser

  moduleLibrary = {}
  urlForModuleLibrary = "https://docs.python.org/3/py-modindex.html"
  response = requests.get(urlForModuleLibrary)
  if response.status_code == 200: #ok
      snakeForWebScarping = htmlParser(response.content, "html.parser")
      moduleNameList = snakeForWebScarping.find_all(class_="xref")

      for module in moduleNameList:
        moduleLibrary[module.text] = f"{module.text}"
  else:
      print(f"ERROR")
      quit()