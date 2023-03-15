
import subprocess

subprocess.run(["git add ."])
subprocess.run(["git commit -m 'message'"])
subprocess.run(["git push -u origin master"])
