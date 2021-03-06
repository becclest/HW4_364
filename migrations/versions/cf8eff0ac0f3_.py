"""empty message

Revision ID: cf8eff0ac0f3
Revises: 
Create Date: 2018-11-24 13:36:35.737582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf8eff0ac0f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_gifs_embedURL', table_name='gifs')
    op.drop_index('ix_gifs_title', table_name='gifs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_gifs_title', 'gifs', ['title'], unique=False)
    op.create_index('ix_gifs_embedURL', 'gifs', ['embedURL'], unique=False)
    # ### end Alembic commands ###
