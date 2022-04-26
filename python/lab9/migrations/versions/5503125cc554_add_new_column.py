"""add_new_column

Revision ID: 5503125cc554
Revises: c1a64f4550c8
Create Date: 2022-04-26 13:46:13.516064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5503125cc554'
down_revision = 'c1a64f4550c8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('leading_hand', sa.String(), nullable=True))


def downgrade():
    op.drop_column('user', 'leading_hand')
