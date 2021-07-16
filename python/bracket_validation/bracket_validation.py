from ll_stack.ll_stack import LL_Stack

def validate_brackets(string):
  temp_stack = LL_Stack()

  for char in string:
    if char in ["(", "{","["]:
      temp_stack.push(char)
    
    if char not in [")", "}", "]"]:
      pass
    else:
      if temp_stack.is_empty():
        return False
      opening_bracket = temp_stack.pop()
      if opening_bracket == "(":
        if char != ")":
          return False
      if opening_bracket == "{":
        if char != "}":
          return False
      if opening_bracket == "[":
        if char != "]":
          return False
  
  if temp_stack.is_empty():
    return True
  return False