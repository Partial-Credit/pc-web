# PC Website
This is the repository for the Partial Credit website. Interested in helping develop it? Then check out the getting started instructions to get a development environment set up.


## Getting Started
These instructions assume you are running Ubuntu Linux 16.0.4+ or your own personal favorite Linux distro. If you do your development on Windows you may need to do some extra work or ask someone for help if you get stuck. OSX users should be able to roughly follow these instructions.



### Installation
#### Git
  * To contibute to the project you'll need to know some version control basics. We are using [Git](https://en.wikipedia.org/wiki/Git). If you've never used Git before your first step should be to learn about it and how to use it. You can find lots of great resources for learning Git here: [https://try.github.io/](https://try.github.io/).
  * Git can be installed by running `sudo apt install git`
#### Python Version 3.5+
  * If you are running Ubuntu or another Linux distro you likely already have Python3 installed. You can check your version number by running `python -V` or install by running `sudo apt install python3`
  * When you install Python pip should be installed with it. [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) is a package manager that makes it easy to install and manage Python libraries and packages

#### Virtualenvwrapper (optional but highly reccomended)
  * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is a tool that allows you to easily create Python virtual environments. Using virtual environments while developing python projects allows each project to have it's own isolated version of dependencies you install, preventing conflicts and overlap.
  * Install by running
  ```$ pip install virtualenvwrapper
  $ export WORKON_HOME=~/.virtualenvs
  $ source /usr/local/bin/virtualenvwrapper.sh
  $ mkvirtualenv pc-web
  ```
 * After installing and creating the virtual environment your terminal should have (pc-web) displayed before your terminal username and machine name such as `(pc-web) alex@<computer-name>: $` This means you have created a virtual enviroment and have it active or are "working inside it". 
  
 * To exit the virtual environment run `deactivate` or exit the terminal window and your terminal should return to normal. To enter back into the environment run `workon pc-web`
 * If you installed virtualenvwrapper ensure you have the `pc-web` environment active before continuing. 
 
#### Django 2.0
  * Django is the webframework the website is built on. After installing everything you should read about it on their [website](https://www.djangoproject.com/) to get a general idea and then dive into their exellent [documentation](https://docs.djangoproject.com/en/2.0/). 
  * Install by running `pip install Django` with your virtual environment active
