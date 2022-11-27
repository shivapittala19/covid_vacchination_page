commands:

Migrate data into dtabase: python3 manage.py makemigrations
                           python3 manage.py migrate
To run the server:  python3 manage.py runserver

Go to http://127.0.0.1:8000 to get the home page.

Admin Login:
   create a super user for a database:
      sudo -u postgres createuser <username> -s with password '<password>'
      
    