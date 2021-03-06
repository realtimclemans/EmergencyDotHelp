"""empty message

Revision ID: 0dcbcc7debf7
Revises: d54b539f0d8a
Create Date: 2021-02-20 18:14:58.915868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dcbcc7debf7'
down_revision = 'd54b539f0d8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_people_current_gps_location', table_name='people')
    op.create_unique_constraint(None, 'people', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.create_index('idx_people_current_gps_location', 'people', ['current_gps_location'], unique=False)
    # ### end Alembic commands ###
