"""empty message

Revision ID: 5d52372d4bec
Revises: 64fa61d3ed72
Create Date: 2023-06-22 23:51:24.233687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d52372d4bec'
down_revision = '64fa61d3ed72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_question_create_date'), ['create_date'])
        batch_op.create_unique_constraint(batch_op.f('uq_question_subject'), ['subject'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_question_subject'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_question_create_date'), type_='unique')

    # ### end Alembic commands ###
