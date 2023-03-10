"""empty message

Revision ID: aee141540a78
Revises: 2b8d305f71ff
Create Date: 2023-03-07 21:03:57.486787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aee141540a78'
down_revision = '2b8d305f71ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=True),
    sa.Column('day_description', sa.String(), nullable=True),
    sa.Column('good_day', sa.Boolean(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apitoken', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('apitoken')

    op.drop_table('calendar')
    # ### end Alembic commands ###
