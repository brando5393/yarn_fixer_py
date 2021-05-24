# Yarn Fixer
A python script designed to automate the conversion of scripts in a package.json file that start with yarn to npm to save developers time.
## System Requirements
- Python 3.8.5 or higher | [Download](https://www.python.org/downloads/)
## Installation and Use
In order to get the best experence from Yarn Fixer it is recomended that the script file be placed in a folder or location that is within the host computer's system path environment variable(s), this way it can be accessed and used via the command line from any directory on the host system.  
For information on how to add or edit environment variables, please choose from one of the links below.  
  
**Windows:** https://www.imatest.com/docs/editing-system-environment-variables/#Windows  
**Mac:** https://www.imatest.com/docs/editing-system-environment-variables/#OS_X  
**Linux:** https://www.imatest.com/docs/editing-system-environment-variables/#Linux  
  
  Once this has been done, open up a new terminal and enter: `yarnfixer`  
  then, when prompted enter a filepath to the package.json file that you want to edit.  
  For example: `C:\Users\jdoe\Desktop\my_cool_app\package.json`  
  If however no path is entered, Yarn Fixer will look for a package.json file in the current working directory.  
  That's it your package.json file should be converted to use npm.
  ## Issues
  If you experence issues or other bugs, please submit an issue at: https://github.com/brando5393/yarn_fixer_py/issues/new?assignees=&labels=&template=bug_report.md&title=
