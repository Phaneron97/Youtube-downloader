import subprocess  # subprocess enables programs to be run from .py-file

args = 'youtube-dl.exe ' \
       '--download-archive downloaded.txt ' \
       '-i ' \
       '-o "%(uploader)s/%(upload_date)s - %(title)s - (%(duration)ss) [%(resolution)s].%(ext)s" ' \
       '--batch-file=channel_list.txt'

subprocess.call(args).read()  # calls program with args (exetutable included)
