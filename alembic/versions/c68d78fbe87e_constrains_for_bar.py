"""constrains for bar

Revision ID: c68d78fbe87e
Revises: 8a9ab85c5759
Create Date: 2025-03-07 13:17:26.544947

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c68d78fbe87e"
down_revision: Union[str, None] = "8a9ab85c5759"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    op.create_unique_constraint(
        "uq_business_name_address_type",
        "businesses",
        ["name", "address", "type"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_business_name_address_type", "businesses", type_="unique")
    op.execute("DROP EXTENSION IF EXISTS pg_trgm")
