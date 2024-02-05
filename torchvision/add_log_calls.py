# run to add logger method when certain things are called in the python file

# test calls to look for

# Log.write_call(currentframe(), "") 
calls = ["
py_file = os.open("models/resnet.py", "a")
file_lines = os.readlines(py_file)

for call in 
