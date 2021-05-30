"""empty message

Revision ID: 3091ca2e35c8
Revises: 3516ccf3ade0
Create Date: 2021-05-30 11:48:24.541985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3091ca2e35c8'
down_revision = '3516ccf3ade0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###