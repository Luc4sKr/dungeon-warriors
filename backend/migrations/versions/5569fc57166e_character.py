"""character

Revision ID: 5569fc57166e
Revises: e68d1f1d7c26
Create Date: 2023-08-26 10:47:07.119588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5569fc57166e'
down_revision = 'e68d1f1d7c26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('life', sa.Integer(), nullable=False),
    sa.Column('strength', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.Column('weapon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['weapon_id'], ['weapon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###
