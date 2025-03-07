from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

"""booked column for space

Revision ID: 299ffef9aa3d
Revises: 4194848bec00
Create Date: 2025-03-07 09:38:46.097591

"""


# revision identifiers, used by Alembic.
revision: str = "299ffef9aa3d"
down_revision: Union[str, None] = "4194848bec00"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "spaces",
        sa.Column("available", sa.Boolean(), server_default="True", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("spaces", "available")
    pass
