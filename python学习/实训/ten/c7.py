import re 
s='PythonPythonPythonPythonPython'
r=re.findall('(Python){3}',s)
print(r)