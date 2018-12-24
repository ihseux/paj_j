"""followers addition

Revision ID: 875ce014d38b
Revises: 09aba55594c0
Create Date: 2018-12-24 22:23:53.072710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '875ce014d38b'
down_revision = '09aba55594c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
