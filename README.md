# travelloWebApp
Web Application to travel around India - developed using Django Framework (Obfuscated)

Note:
1. You need to have Python and Django installed on your Device 
(if not, 
        -> Install Python:
   i)   Download Python at https://www.python.org/downloads/ 
   ii)  Set path to configure with your system
        -> Install pip:
   i)   Download pip from https://bootstrap.pypa.io/get-pip.py
   ii)  Open a command prompt and navigate to the folder containing get-pip.py.
   iii) Run the following command: python get-pip.py
   iv)  Run the command: pip -h (If you see the help text for pip then you have pip installed)
   v)   Check the pip version: using pip -V or pip --version
        -> Install Django:
   i)   Run the command: pip install django
   ii)  Check the version using: django-admin --version

2. Install Virtual Environment Wrapper using: pip install virtualenvwrapper

3. Create a virtual environment using command: virtualenv <environment name>

4. Clone the project from the repository to Visual Studio platform. (If you feel VS is heavy, download to work at Sublime Text or Notepad++)

5. I've set the database as postgres since I worked on PostgreSQL 12 (if you are working at MySQL or SQLite, change accordingly in the settings.py file)

6. Create a database and run the command: python manage.py makemigrations (to migrate the static file changes to at the project folder)
      Run the command: python manage.py collectstatic (whenever you make changes in the static folder)
      
7. Run the command: python manage sqlmigrate <AppName> <migration number> 
(In my case AppName was travello and Migration number is 0001 (New Migration numbered files will be created at the App directory whenver you make migrations))

8. Run the command: python manage.py migrate (to create table in your Database)

9. Run the command: python manage.py createsuperuser (to create a Super User for the Administration of the project)

10. Run the command: python manage.py runserver (which starts the server with server URL)

11. Open the Application in your browser using the URL: <HostID/Hostname>:<portnumber>/<appname>
    [127.0.0.1:8000/travello] in my case.

If you want to add more objects, open URL: <HostID/Hostname>:<portnumber>/<admin>, login as a super user
then add Destinations on your own which automatically gets reflected on the home page.

