#!/usr/bin/env python3

class MyString:

  def __init__(self, value=""):

    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else: 
      print("The value must be a string.")
    
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
      count = 0
      string = self.value.replace("!", ".")
      string = string.replace("?", ".")
      sentence_list = string.split(".")
      
      for sentence in sentence_list:
          if len(sentence.strip()) > 0:  # Check if the sentence is not empty
              count += 1
      
      return count
