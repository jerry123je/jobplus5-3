"""empty message

Revision ID: 8783586b8fd0
Revises: 02dd78f10cc1
Create Date: 2018-04-17 13:06:09.153219

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8783586b8fd0'
down_revision = '02dd78f10cc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('companyHomepage', sa.String(length=1024), nullable=True))
    op.drop_column('user', 'compangHomepage')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('compangHomepage', mysql.VARCHAR(length=1024), nullable=True))
    op.drop_column('user', 'companyHomepage')
    # ### end Alembic commands ###
