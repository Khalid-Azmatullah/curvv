def clearCache():
  from pathlib import Path
  path = Path(".")
  for pycFile in path.rglob("*.pyc"):
      pycFile.unlink()
  for pycacheDir in path.rglob("__pycache__"):
      pycacheDir.rmdir()
