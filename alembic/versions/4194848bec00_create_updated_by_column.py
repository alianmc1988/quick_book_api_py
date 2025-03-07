import sqlalchemy as sa
from typing import Sequence, Union

from alembic import op

"""create updated-by column

Revision ID: 4194848bec00
Revises: 0e620ff84abb
Create Date: 2025-03-06 15:02:47.797557

"""


# revision identifiers, used by Alembic.
revision: str = "4194848bec00"
down_revision: Union[str, None] = "0e620ff84abb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("updated_by", sa.UUID, nullable=True),
    )
    op.add_column(
        "roles",
        sa.Column("updated_by", sa.UUID, nullable=True),
    )
    op.add_column(
        "businesses",
        sa.Column("updated_by", sa.UUID, nullable=True),
    )
    op.add_column(
        "business_social_medias",
        sa.Column("updated_by", sa.UUID, nullable=True),
    )
    op.add_column(
        "spaces",
        sa.Column("updated_by", sa.UUID, nullable=True),
    )


def downgrade() -> None:
    op.drop_column("users", "updated_by")
    op.drop_column("roles", "updated_by")
    op.drop_column("businesses", "updated_by")
    op.drop_column("business_social_medias", "updated_by")
    op.drop_column("spaces", "updated_by")
