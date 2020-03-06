"""add blacklist table

Revision ID: a6d020de9fb0
Revises: 83342ffe0575
Create Date: 2020-03-04 23:16:35.131000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6d020de9fb0'
down_revision = '83342ffe0575'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('appId', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('appId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
