"""create hello table

Revision ID: bec99769a579
Revises: 
Create Date: 2025-12-24 01:39:08.657730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bec99769a579'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "hello",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("message", sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table("hello")
