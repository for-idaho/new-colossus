"""empty message

Revision ID: 3f7d48bb9e93
Revises: f61e52976d0b
Create Date: 2018-03-27 08:54:20.454545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f7d48bb9e93'
down_revision = 'f61e52976d0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_token',
    sa.Column('jti', sa.String(length=64), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('jti')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_token')
    # ### end Alembic commands ###