import re
def capital_words_spaces(txt):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))