# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()





class ContentRating(db.Model):
    __tablename__ = 'content_rating'

    appId = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(45), nullable=False)
    Content_Rating_appId = db.Column(db.Integer, nullable=False)

class VersionManagement(db.Model):
    __tablename__ = 'version_management'

    appId = db.Column(db.Integer, primary_key=True)
    current_version = db.Column('current version', db.String(45), nullable=False)
    android_version = db.Column(db.String(100))

class AppInfo(db.Model):
    __tablename__ = 'app_info'

    appId = db.Column(db.ForeignKey(u'category.appId'), db.ForeignKey(u'version_management.appId'), db.ForeignKey(u'content_rating.appId'), primary_key=True)
    appName = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float)
    Price = db.Column(db.Float)

    content_rating = db.relationship(u'ContentRating', uselist=False, primaryjoin='AppInfo.appId == ContentRating.appId', backref=u'app_infos')
    version_management = db.relationship(u'VersionManagement', uselist=False, primaryjoin='AppInfo.appId == VersionManagement.appId', backref=u'app_infos')








