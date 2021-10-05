# from app import app
from app import create_app, db
# .....
from flask_script import Manager,Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand


app = create_app('production')
app.app_context().push() 
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql+psycopg2://evance:0701003610sue@localhost/pitch2"
db.init_app(app)



app.config["SQLALCHEMY_TRACK_NODFICATIONS"]= False
manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    app.run(debug=True)
