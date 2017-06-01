import re
text = 'His fall was not a sma$%$%$%$%$$ll one.'
text = re.sub('[!@#$%^&*]', '', text)
print(text)
