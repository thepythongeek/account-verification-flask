﻿from flask.ext.testing import TestCase
from flask.ext.sqlalchemy import SQLAlchemy
from account_verification_flask import app, db
from account_verification_flask.models.models import *
import account_verification_flask.views

class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        #db.session.add(User("admin", "ad@min.com", "admin"))
        #db.session.commit()

    def tearDown(self):
        #db.session.remove()
        db.drop_all()