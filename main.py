it doesn't contain spaces,
it contains the @ symbol,
after @, there's a dot, but in a correct address a dot shouldn't stand immediately after @,
(@. should not be in the string).
Note that dots may also occur before @!

The function should return True if all of the conditions are true, and False otherwise.

def check_email(string):
    return "@" in string and " " not in string and "@." not in string and string.find(".", string.index("@")) > 0
  
def check_email(string):
    checks = all(e in string if i < 2 else e not in string for i, e in enumerate(['@', '.', '@.', ' ']))
    return checks and string.rfind('.') > string.find('@')
