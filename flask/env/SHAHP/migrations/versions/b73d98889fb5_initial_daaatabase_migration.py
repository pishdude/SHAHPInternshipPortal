"""initial daaatabase migration

Revision ID: b73d98889fb5
Revises: 53745de6bcdc
Create Date: 2020-03-12 18:19:47.296000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73d98889fb5'
down_revision = '53745de6bcdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('idAgency', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('type', sa.String(length=45), nullable=True),
    sa.Column('description', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('idAgency')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agency')
    # ### end Alembic commands ###
