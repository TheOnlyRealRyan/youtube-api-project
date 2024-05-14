This desktop application will implement features from the python-youtube library, pytube library and use the YouTube DATA API v3.



Issues:

With pytube issue #1199 https://github.com/pytube/pytube/issues/1199:

After pip install -r Requirements.txt 

in the Cipher.py file in the pytube library, replace line 30: 

"var_regex = re.compile(r"^\w+\W")" 

with 

"var_regex = re.compile(r"^\$*\w+\W")"

https://developers.google.com/youtube/v3/docs/

If Error: FileNotFoundError: [WinError 2] The system cannot find the file specified

then:

The location of ffmpeg/bins has to be added to your environment variables

For Windows, download ffmpeg-git-full.7z from https://www.gyan.dev/ffmpeg/builds/ or navigate from https://ffmpeg.org to the before mentioned site.

Extract.

Rename to ffmpeg

Move to C:

Add ffmpeg/bins to environment variables

