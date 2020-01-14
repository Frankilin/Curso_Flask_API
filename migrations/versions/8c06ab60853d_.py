"""empty message

Revision ID: 8c06ab60853d
Revises: 366eb8c2ee80
Create Date: 2020-01-14 15:51:20.301491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c06ab60853d'
down_revision = '366eb8c2ee80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarefa', sa.Column('projeto_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tarefa', 'projeto', ['projeto_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tarefa', type_='foreignkey')
    op.drop_column('tarefa', 'projeto_id')
    # ### end Alembic commands ###