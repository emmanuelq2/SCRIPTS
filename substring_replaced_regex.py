""" import re
from xxlimited import new
 """
def replace_substring_regex(text, old, new):
    import re
    result = []

    re.substring = re.escape(old)
    result = re.sub(re.substring, new, text)
    return result

print(replace_substring_regex("hello world", "world", "friend"))
print(replace_substring_regex("i love coding", "code", "craft"))
print(replace_substring_regex("it is a beautiful day", "beautiful", "gloomy"))
print(replace_substring_regex("practice makes perfect", "perfect", "better"))
print(replace_substring_regex("keep calm and carry on", "carry on", "code on"))
print(replace_substring_regex("long text long text", "long", "short"))