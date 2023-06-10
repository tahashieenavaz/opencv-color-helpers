import subprocess

def copy(text):
    subprocess.run("pbcopy", text=True, input=text)
