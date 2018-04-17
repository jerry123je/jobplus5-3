"""empty message

Revision ID: 4e73c7fae445
Revises: 
Create Date: 2018-04-16 21:39:55.499615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e73c7fae445'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deliveryJob', sa.Integer(), nullable=False),
    sa.Column('deliveryCompany', sa.Integer(), nullable=False),
    sa.Column('deliveryJobseeker', sa.Integer(), nullable=False),
    sa.Column('deliveryStatus', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jobName', sa.String(length=255), nullable=False),
    sa.Column('jobTag', sa.String(length=255), nullable=False),
    sa.Column('jobDescription', sa.String(length=4096), nullable=False),
    sa.Column('jobAddress', sa.String(length=1024), nullable=False),
    sa.Column('jobSalaryL', sa.Integer(), nullable=False),
    sa.Column('jobSalaryH', sa.Integer(), nullable=False),
    sa.Column('jobExperience', sa.String(length=255), nullable=False),
    sa.Column('jobEducation', sa.String(length=255), nullable=False),
    sa.Column('jobCompany', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    op.drop_table('delivery')
    # ### end Alembic commands ###