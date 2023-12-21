"""empty message

Revision ID: 6e15785ae44f
Revises: c967fe31d388
Create Date: 2023-12-21 15:16:03.481085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e15785ae44f'
down_revision: Union[str, None] = 'c967fe31d388'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('test_cod', sa.BigInteger(), nullable=True))
    op.drop_column('test', 'code ')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('code ', sa.BIGINT(), autoincrement=False, nullable=True))
    op.drop_column('test', 'test_cod')
    # ### end Alembic commands ###
