"""initial database migration

Revision ID: dc055e8696dd
Revises: 
Create Date: 2021-03-01 12:09:58.676720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc055e8696dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('intervention',
    sa.Column('code', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ref_client', sa.String(length=50), nullable=False),
    sa.Column('piece', sa.String(length=100), nullable=True),
    sa.Column('probleme', sa.String(length=250), nullable=True),
    sa.Column('reussi', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('code'),
    sa.UniqueConstraint('ref_client')
    )
    op.create_table('technicien',
    sa.Column('code', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('intervention', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('technicien')
    op.drop_table('intervention')
    # ### end Alembic commands ###
