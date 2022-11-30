# ASTormTrooper
*ASTT* is a simple Linter, small and fast that reads dictionaries as configuration.<br>
It accepts functions and lambdas as custom rules. Sometimes, filters don't need much code.
<br><br>
![stats](https://img.shields.io/pypi/dm/ASTormTrooper)

# How to download
```py
# GIT+PIP
pip install git+https://github.com/ZSendokame/ASTormTrooper.git

# PIP
pip install ASTormtrooper
```

# How to use
You can call ASTT with:<br>
`python -m astt`

### Flags
-c: Change configuration file.<br>
-e: Files to exclude. (Example: `-e "excluded.py,otherfile.py"`)<br>
-a: Path to start the scan from. (Default: .)

# Examples
https://gist.github.com/ZSendokame/816c1d6ea9b78840254e70fd5e90d34a