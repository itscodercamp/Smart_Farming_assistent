import os
import webbrowser
# The path to the directory containing the virtual environment and manage.py
project_path = ".\\Project_Files\\MainProject\\"
# The URL to open in the browser
url = "http://127.0.0.1:8000/"

# Open the specified URL in the default browser
webbrowser.open(url)
# The command to run in the virtual environment
command = "python manage.py runserver"
# Change to the project directory
os.chdir(project_path)
# Activate the virtual environment and run the specified command
os.system(f"call {command}")
