import subprocess

downloadCommand = 'wget https://gssc.esa.int/navipedia/images/thumb/a/a9/Example.jpg/200px-Example.jpg'.split(' ')
command = 'ffmpeg -loop 1 -i 200px-Example.jpg -t 7 test.mp4'.split(' ')

subprocess.run(downloadCommand)
subprocess.run(command)