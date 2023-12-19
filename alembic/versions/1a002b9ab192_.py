"""empty message

Revision ID: 1a002b9ab192
Revises: f4328bc31d19
Create Date: 2023-12-02 15:54:56.114125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a002b9ab192'
down_revision: Union[str, None] = 'f4328bc31d19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('photo', sa.TEXT(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    # ### end Alembic commands ###