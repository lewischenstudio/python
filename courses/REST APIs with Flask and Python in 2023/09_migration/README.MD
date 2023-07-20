## Section 9: Database migrations with Alembic and Flask-Migrate

#### Table of Contents
- Why use database migrations at all?
- How to add Flask-Migrate to our Flask app
- Initialize your database with Flask-Migrate
- Change SQLAlchemy models and generate a migration
- Mannually review and modify database migrations


### Why use database migrations?

Adding columns to your models, or even new models entirely, will require that the existing database tables and the model definitions are synchronized. To synchronize both ends, we cannot rely only on SQLAlchemy. We need to use Alembic. 

Alembic can detect the changes to the models -- what steps are necessary to "upgrade" the database so it matches the new models -- modify the database following the upgrade steps, track each of these migrations, which is essential to keeping records of changes to models and the database. We can use Alembic to create the tables from scratch, simply by applying the migrations one at a time until we reach the latest/current one.


### Initialize your database with Flask-Migrate
Initialize the database with the following command line
```
flask db init
----------------
Creating directory C:\Users\lcyc2\dev\python\flask\09_migration\migrations ...  done
Creating directory C:\Users\lcyc2\dev\python\flask\09_migration\migrations\versions ...  done
Generating C:\Users\lcyc2\dev\python\flask\09_migration\migrations\alembic.ini ...  done
Generating C:\Users\lcyc2\dev\python\flask\09_migration\migrations\env.py ...  done
Generating C:\Users\lcyc2\dev\python\flask\09_migration\migrations\README ...  done
Generating C:\Users\lcyc2\dev\python\flask\09_migration\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\\Users\\lcyc2\\dev\\python\\flask\\09_migration\\migrations\\alembic.ini' before proceeding.
```
This command will create two folders `instance` and `migratinons`. In folder `instance`, there is a file `database.db` to hold the database. In folder `migrations`, there are multiple folders and files to keep track of the models.

Run the command line below to let Alembic detect any changes in the models and database.
```
flask db migrate
----------------
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'stores'
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added table 'items'
INFO  [alembic.autogenerate.compare] Detected added table 'tags'
INFO  [alembic.autogenerate.compare] Detected added table 'items_tags'
Generating C:\Users\lcyc2\dev\python\flask\09_migration\migrations\versions\254255afef79_.py ...  done
```

Run the command line below to make the changes to the database `database.db`
```
flask db upgrade
----------------
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 254255afef79, empty message
```

The files `migrations/versions/**.py` keep track of the versions of migrations so that we know which version of the database we are referring to for future migrations.


### Change SQLAlchemy models and generate a migration
Add `description = db.Column(db.String)` to the `ItemModel`. Run the commands to change the database.
```
flask db migrate
----------------
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'items.description'
Generating C:\Users\lcyc2\dev\python\flask\09_migration\migrations\versions\956daf07cb60_.py ...  done

flask db upgrade
----------------
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 3150bd4949f8 -> 956daf07cb60, empty message
```


### Mannually review and modify database migrations
In case you need to do this, go to the migration files and do something like the following
```python
def upgrade():
  ...
  op.execute("UPDATE invoices SET enable_downloads = False")

def downgrade():
  op.drop_column("invoices", "enable_downloads")
```
It is highly recommended that you don't do this in your migration files. Any changes you want to apply to the database should go through the models.

