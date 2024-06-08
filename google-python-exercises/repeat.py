def repeat(s, exclaim)
  result = s + s + s
  if exclaim:
    result = result + '!!!'
  return result