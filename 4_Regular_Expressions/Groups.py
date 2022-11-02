import re
from datetime import date
year = str(date.today())[:4]

strn = 'copyright 2005-2006'
print(re.sub(
   r'((19|20)[0-9]{2})-((19|20)[0-9]{2})', r'\1-' + year,
   strn))
