# Cheers!
This is the main repository for Cheers Food. 
https://cheersapp.io/

### Development Environment
***
+ Language: Python 3.8.5
+ IDE: Visual Studio Code

### Development Environment Setup Instructions
***
+ [Visual Studio Code](https://code.visualstudio.com/)
+ [Git Version Control](https://git-scm.com/downloads)

Visual Studio Code is a very intuitive and simple to use IDE with terminal integration and support for various languages and frameworks. 

Git is used for software version control. 

1. Download and install [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
2. Downloand and install [git](https://git-scm.com/downloads)
3. When you have Python installed make a new virtual environment. Open a new Visual Studio Code terminala and run:
    1. `virtualenv venv`
    2. Activate virtual environent. Windows: `./venv/Scripts/activate` MacOS: `source venv/bin/activate`
    3. Your virtual environment is now activated. All packages you install in your virtual environment will be separate from the rest of your OS.
4. Clone, or download, the git repository by clicking the "Source Control" option on the far left sidebar, and click "Clone Repository". Paste in the url of the Cheers github repository (https://github.com/CheersFood/cheers.git). You may be asked to login to your GitHub account. Wait for the download to complete. 
5. In a terminal, install packages from requirements.txt using: `pip install requirements.txt`
6. Open `app.yaml` and insert the TWILIO_ACCOUNT_SID and the TWILIO_AUTH_TOKEN. These can be found on the Twilio console. You cannot use Twilio programatically without this information. 
7. Download json file containing google keys and put in working directory. This is required to communicate with Google Sheets and can be found in the Google Cloud Console. Ask Jack for more information on this.  
8. Set GOOGLE_APPLICATION_CREDENTIALS environment variable to location of json file containing google keys. 
    - e.g. $env:GOOGLE_APPLICATION_CREDENTIALS="some_filepath/somefile.json"

You have now prepared your development environment. 

### Testing
***
1. To use the Cheers Twilio Test Number, you must setup an ngrok server. Download ngrok and run `./ngrok http 5000`. This will start a new http server that lasts for 2 hours. 
2. Copy the https url and past it into the "Messaging" webhook on Twilio for the Test Number. 
3. Run `python main.py` in a VS Code terminal. You can now send messages to the Test Number and output will appear in the terminal. 

Direct questions to Jack. 

### Git Workflow
***
Git is used for version control. Please familiarize yourself with the basics
using [this simple guide][1]. The general workflow will closely resemble the
branch model in [this overview][2].

[1]: http://rogerdudler.github.io/git-guide/
[2]: https://nvie.com/posts/a-successful-git-branching-model/

There are many ways to use Git, so this guide will not give detailed
instructions. PyCharm has several tools to make changes via version control,
but you can also use basic CLI tools. Look up the appropriate documentation
based on whatever method you wish.

#### Creating a Development Branch
1. Checkout master branch.
2. Create a new branch, naming it in the style of `<name>/dev`.
    (Ex: `daniel/dev`.)

This will be your "main" branch to base your feature branches off of.

#### Creating a Feature Branch
1. Checkout your development branch.
2. Create a new branch, naming it in the style of `<name>/<feature>`.
    (Ex: `daniel/magnetometer`.)

Anytime you work on a new feature, create a feature branch for it. That way,
you can resolve any merge issues all at once when you are prepared to merge
back to the development branch.

#### Committing and Pushing Code
1. Commit your code often. Give a brief summary of your changes in the commit
    description.
2. When you're done for the day, push your code to the GitHub repository.

#### Merging to Development Branch
1. Whenever you complete work on a feature branch, merge it back into your
    development branch.
2. Delete your feature branch once merged; your changes will reflect in your
    development branch.

#### Creating a Pull Request
***DO NOT MERGE BACK TO MASTER ON YOUR OWN.***

1. Once the code in your development branch has been fully-tested, create a
    pull request on GitHub.
2. The team lead will review your code and merge it to the master branch.

### Dos and Donts
***
* Follow [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
* Code readability over performance
* Commit often with meaningful commit message
* Work on a branch off the master and create pull request when ready for merge

### References
***
+ [Unix Command Line Cheats](https://www.git-tower.com/blog/command-line-cheat-sheet/)
+ [Git Cheat Sheet](https://www.git-tower.com/blog/git-cheat-sheet/)
+ [Git branch usage](https://stackoverflow.com/questions/10009175/how-to-properly-use-git-and-branches)
+ [Python 3 Official Docs and Tutorials](https://docs.python.org/3/)
+ [Python Structure/Good Practice Guide](http://docs.python-guide.org/en/latest/writing/structure/)
+ [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
+ [Sphinx/Python Doc Auto Generation](https://pythonhosted.org/an_example_pypi_project/sphinx.html)
