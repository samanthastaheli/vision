"""
writes to a txt file what is called
"""

import os
from inspect import currentframe 

class Log:
  def __init__(self):
    self.filename = "log.txt"
    self.save_path = f"{os.cwd}/{self.filename}"
    
  def __call__(self):
    try:
      f = open(self.filename, "x")
    self.file = open(self.fileame, "a") # a is append so will add a line to the file instead of write over
    
  def check_filepath(self):
    if os.path.isdir(self.save_path):
      pass
    else:
      os.mkdir(self.save_path)

  def write_call(self, frame, call_description):
    lineno = frame.lineno
    name = frame.filename
    func = frame.function
    self.file.write(f"{call_description}, filename: {name}, function: {func}, line: {lineno}")

  def __exit__(self):
    self.file.close()
