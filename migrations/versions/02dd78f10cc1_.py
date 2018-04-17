"""empty message

Revision ID: 02dd78f10cc1
Revises: 18110ea8a394
Create Date: 2018-04-16 21:56:31.063249

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '02dd78f10cc1'
down_revision = '18110ea8a394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('jobseekerExperience', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('userPhone', sa.String(length=15), nullable=True))
    op.drop_column('user', 'jobseekerName')
    op.drop_column('user', 'jobseekerPhone')
    op.drop_column('user', 'userExperience')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('userExperience', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('jobseekerPhone', mysql.VARCHAR(length=15), nullable=True))
    op.add_column('user', sa.Column('jobseekerName', mysql.VARCHAR(length=20), nullable=True))
    op.drop_column('user', 'userPhone')
    op.drop_column('user', 'jobseekerExperience')
    # ### end Alembic commands ###
