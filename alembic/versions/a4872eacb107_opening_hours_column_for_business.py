"""opening_hours column for business

Revision ID: a4872eacb107
Revises: c68d78fbe87e
Create Date: 2025-03-07 13:58:13.536184

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "a4872eacb107"
down_revision: Union[str, None] = "c68d78fbe87e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "businesses",
        sa.Column(
            "opening_hours", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )


def downgrade() -> None:
    op.drop_column("businesses", "opening_hours")
