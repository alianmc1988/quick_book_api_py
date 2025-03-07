"""create master field

Revision ID: 0e620ff84abb
Revises: 34e1a42f110a
Create Date: 2025-03-06 10:25:16.826981

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "0e620ff84abb"
down_revision: Union[str, None] = "34e1a42f110a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("is_master", sa.Boolean, server_default="False", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("users", "is_master")
    pass
