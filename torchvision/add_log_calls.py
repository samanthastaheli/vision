# run to add logger method when certain things are called in the python file

# test calls to look for

# Log.write_call(currentframe(), "") 
calls = ["ImageClassification", "_log_api_usage_once", 
         "register_model", "Weights", "WeightsEnum", 
         "_IMAGENET_CATEGORIES", "_ovewrite_named_param", 
         "handle_legacy_interface"]

py_file = os.open("models/resnet.py", "a")
file_lines = os.readlines(py_file)

for call in calls:
  for line in file_lines:
    if call in line:
      
