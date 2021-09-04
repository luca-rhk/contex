# ContEx

This is the repository of the ContEx system, a webservice to enable continuous experimentation with IFML models and their according final UIs.

## Local installation

You need to install the Django Framework on your computer. You can get further information [here](https://www.djangoproject.com/).

## Database handling
### Migrations

Once the database models are changed you need to execute the following command to let Django generate a migration for you:

```python .\manage.py makemigrations contex```

To execute the migration into the database, execute the following command:

```python .\manage.py sqlmigrate contex 000X```

where `000X` represents the generated migration prefix.

## Migration of project/code changes

To reflect code/project changes in the server, run

```python .\manage.py migrate```

## Start the local server

Run the local Django Webserver with the following command:

```python .\manage.py runserver```