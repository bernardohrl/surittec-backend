import unittest
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
from project.seed_database import seed_database


cli = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreatedb():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def seed():
    seed_database()


if __name__ == '__main__':
    cli()
