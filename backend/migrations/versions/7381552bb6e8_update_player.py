"""update player

Revision ID: 7381552bb6e8
Revises: 3cde3f4eb0af
Create Date: 2023-08-22 23:03:54.148269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7381552bb6e8'
down_revision = '3cde3f4eb0af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.add_column(sa.Column('strength', sa.Integer(), nullable=False))
        batch_op.drop_column('damage')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.add_column(sa.Column('damage', sa.INTEGER(), nullable=False))
        batch_op.drop_column('strength')

    # ### end Alembic commands ###
