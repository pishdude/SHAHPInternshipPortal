"""add blacklist table

Revision ID: af47d2f6ca0e
Revises: b7a9d4b6db56
Create Date: 2020-03-04 22:58:47.644000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'af47d2f6ca0e'
down_revision = 'b7a9d4b6db56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('app_info')
    op.drop_table('content_rating')
    op.drop_table('category')
    op.drop_table('version_management')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('version_management',
    sa.Column('appId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('current version', mysql.VARCHAR(length=45), nullable=False),
    sa.Column('android_version', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('appId'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('category',
    sa.Column('appId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('category', mysql.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('appId'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('content_rating',
    sa.Column('appId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('rating', mysql.VARCHAR(length=45), nullable=False),
    sa.Column('Content_Rating_appId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('appId'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('app_info',
    sa.Column('appId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('appName', mysql.VARCHAR(length=300), nullable=False),
    sa.Column('rating', mysql.FLOAT(), nullable=True),
    sa.Column('Price', mysql.FLOAT(), nullable=True),
    sa.ForeignKeyConstraint(['appId'], ['category.appId'], name=u'categorykey'),
    sa.ForeignKeyConstraint(['appId'], ['content_rating.appId'], name=u'contentkey'),
    sa.ForeignKeyConstraint(['appId'], ['version_management.appId'], name=u'versionkey'),
    sa.PrimaryKeyConstraint('appId'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('user')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
