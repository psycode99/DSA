def power_of_number(base, exp):
  assert base >= 0 and isinstance(base, int), "base must be a vlaid positive integer"
  assert exp >= 0 and isinstance(exp, int), "exponent must be a valid positive integer"

  if exp == 0:
    return 1
  else:
    return base * power_of_number(base, exp-1)
    
print(power_of_number(2, 4))