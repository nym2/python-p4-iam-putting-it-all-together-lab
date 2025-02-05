"""empty message

Revision ID: 7359ae5145a9
Revises: 66c7626408f9
Create Date: 2025-02-05 20:49:07.947291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7359ae5145a9'
down_revision = '66c7626408f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
