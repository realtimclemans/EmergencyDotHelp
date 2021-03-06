"""empty message

Revision ID: 44ef8e725244
Revises: 796b6133426b
Create Date: 2021-03-08 22:09:16.590136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44ef8e725244'
down_revision = '796b6133426b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('preferred_psychiatric_inpatient_facility', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'preferred_psychiatric_inpatient_facility')
    # ### end Alembic commands ###
