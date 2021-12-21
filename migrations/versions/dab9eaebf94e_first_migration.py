"""first migration

Revision ID: dab9eaebf94e
Revises: 
Create Date: 2021-12-21 20:57:07.675542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dab9eaebf94e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('radio_channel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('cover_url', sa.String(length=1000), nullable=True),
    sa.Column('radio_stream_url', sa.String(length=1000), nullable=True),
    sa.Column('is_active', sa.Boolean, default=False, nullable=True),
    sa.Column('is_popular', sa.Boolean, default=False, nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('nickname', sa.String(length=12), nullable=True),
    sa.Column('roles', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('radio_channel')
    # ### end Alembic commands ###
