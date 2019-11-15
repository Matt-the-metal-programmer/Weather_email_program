import os
import time
import sys

readmedata = input("please input whatever data you would like in your readme, do not include \" or \' ")
readme = "sudo echo '"+readmedata+"\'>> README.md"
os.system(readme)
os.system('sudo git clone https://github.com/Matt-the-metal-programmer/GIT-auto.git')
os.system('sudo git init')

os.system('sudo git add .')
os.system('sudo git commit -m "Initial commit"')
remoteorigin = input("please paste the remote origin URL that github provided to you when you created a repository")

reorigin = "sudo git remote add origin "+remoteorigin
os.system(reorigin)
os.system("sudo git push -u origin master")
