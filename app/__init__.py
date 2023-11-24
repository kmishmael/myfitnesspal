#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_restful import Api
from .api.users import UsersResource

from .instance import app

api = Api(app)

api.add_resource(UsersResource, '/users', '/users/<int:user_id>')
