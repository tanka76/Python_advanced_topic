import re
import re
pattern=r'Cookies'
seq='Cookies'
if re.match(pattern,seq):
    print("match")
else:
    print("not match")