"""empty message

Revision ID: 430945e399e9
Revises: d077601a49a9
Create Date: 2023-05-08 15:23:34.298598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430945e399e9'
down_revision = 'd077601a49a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
