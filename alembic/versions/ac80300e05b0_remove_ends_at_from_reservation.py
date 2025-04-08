"""remove ends_at from reservation

Revision ID: ac80300e05b0
Revises: 4194848bec00
Create Date: 2025-03-07 16:31:11.034460

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "ac80300e05b0"
down_revision: Union[str, None] = "4194848bec00"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("reservations", "ends_at")


def downgrade() -> None:
    op.add_column(
        "reservations",
        sa.Column(
            "ends_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
