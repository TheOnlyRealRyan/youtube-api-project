This desktop application will implement features from the python-youtube library, pytube library and use the YouTube DATA API v3.

With pytube issue #1199 https://github.com/pytube/pytube/issues/1199:

After pip install -r Requirements.txt 

in the Cipher.py file in the pytube library, replace line 30: 

"var_regex = re.compile(r"^\w+\W")" 

with 

"var_regex = re.compile(r"^\$*\w+\W")"

https://developers.google.com/youtube/v3/docs/