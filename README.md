# PC Website
This is the repository for the Partial Credit website. Interested in helping develop it? Then check out the getting started instructions to get a development environment set up.


## Getting Started
These instructions assume you are running Ubuntu Linux 16.0.4+ or your own personal favorite Linux distro. If you do your development on Windows you may need to do some extra work or ask someone for help if you get stuck. OSX users should be able to roughly follow these instructions.



### Installation
#### Git
  * To contibute to the project you'll need to know some version control basics. We are using [Git](https://en.wikipedia.org/wiki/Git). If you've never used Git before your first step should be to learn about it and how to use it. You can find lots of great resources for learning Git here: [https://try.github.io/](https://try.github.io/).
  * Git can be installed by running `sudo apt install git`
#### Python Version 3.5+
  * If you are running Ubuntu or another Linux distro you likely already have Python3 installed. You can check your version number by running `python -V` or install by running `sudo apt install python3 python3-dev`
  * When you install Python pip should be installed with it. [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) is a package manager that makes it easy to install and manage Python libraries and packages

#### Virtualenvwrapper (optional but highly reccomended)
  * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is a tool that allows you to easily create Python virtual environments. Using virtual environments while developing python projects allows each project to have it's own isolated version of dependencies you install, preventing conflicts and overlap.
  * Install by running
  ```
  $ pip install virtualenvwrapper
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
  
#### psycopg2
  * psycopg2 is a library that makes it very easy to connect to the database we'll be using. Using Django it is possible to build models and write/read data from the database using only Python, no SQL required.
  * Install by running `pip install psycopg2`
  
#### PostgreSQL
###### Install
  * [PostgreSQL](https://www.postgresql.org/) is a powerful open source object-relational database that pairs nicely with Django. 
  * Install by running `sudo apt install libpq-dev postgresql postgresql-contrib`
###### Configure
  * Now that you have postgres installed you'll need to create a database and configure it with a login and password.
  * To log into an interactive Postgres session run `sudo -u postgres psql` . This should give you a `postgress=# ` prompt in your terminal. 
  * Now we will create a database for the website, run `CREATE DATABASE pcwebsite;`
  * Next we will create a user who can access the database, run `CREATE USER admin WITH PASSWORD '<your password here>';` Make sure you remember the password you create, you will need to add it to the Django settings later. The password will only be used on your local development database.
  * Now we'll make some tweaks to the database settings and give our admin user access, run each of these commands one line at a time:
  ```
  ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
  ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
  ALTER ROLE myprojectuser SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE pcwebsite TO admin;
  ```
  * Now that the database is configured you can exit the prompt by typing `\q`
  
### Clone the Git Repository
  * You're almost finished! Now it's time to download the git repository onto your computer. 
  * You can clone the repository using the green "Clone or download" button or by running `git clone https://github.com/Partial-Credit/pc-web.git` Note that running the clone command will download the repository folder into whatever folder your terminal is currently CDed into, so check that the location is where you want to put the files before running the command.
  
### Update Django Settings
  * For security purposes and to pervent version control conflicts the specific database connection settings are not hardcoded into the Django settings file, instead they are read in from a file. This file is ignored by Git so that your settings don't get overwritten by someone else's which means the file won't exist in the repositry after cloning. I have written a script to quickly generate the settings file for you.
  * CD into the pc-web directory you just cloned and run the initial-setup script by running `python3 initial-setup.py` . The script will prompt you for the database name, user, and password you set. Assuming you used the same db and user name as the guide, you can just hit enter to use the default values for those fields.
  
### Migrate Database Changes
  * Now that the Django settings are configured, we can migrate the project data structures to our database and test out the server. Now that Django is properly configured we will use the manage.py program to controll the Django server (starting, stopping, maintenance, etc.).
  * From within the pc-web project folder run `./manage.py makemigrations` This will tell Django to workout what new changes have been made in the project that haven't been updated on the database yet, these changes are called Migrations. Because your database is empty after creating it Django will have lots of things to update in the Database.
  * Now that the migrations have been created/calculated we need to tell Django to go ahead and apply the changes. Run `./manage.py migrate`
  
### Final Step! Run the Server
  * Good job, you made it through the guide! At this point you should be ready to run the server!
  * The Django server is started by running `./manage runserver` This will start Django running on your computer on port :8000 by default. You can access the site by pointing your browser to `localhost:8000`
  * If the server starts up correctly give yourself a pat on the back, you're ready to start developing! If you get errors or something goes wrong try looking over the guide to make sure you didn't miss a step and then reach out and see if someone can help you if you can't work out the error. 
