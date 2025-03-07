"""featureToggle for business

Revision ID: 06b4a66127e9
Revises: 299ffef9aa3d
Create Date: 2025-03-07 10:30:08.862259

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "06b4a66127e9"
down_revision: Union[str, None] = "299ffef9aa3d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "business_feature_toggles",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "feature_name", postgresql.ENUM("BOOKING", name="feature_toggle_enum")
        ),
        sa.Column("business_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "deleted_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["business_id"],
            ["businesses.id"],
            name="business_feature_toggles_business_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="business_feature_toggles_pkey"),
        sa.UniqueConstraint(
            "feature_name", "business_id", name="feature_name_business_id_key"
        ),
        postgresql_ignore_search_path=False,
    )
    op.create_index(
        "ix_business_feature_toggles_id",
        "business_feature_toggles",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_business_feature_toggles_id", table_name="business_feature_toggles"
    )
    op.drop_table("business_feature_toggles")
    op.execute("DROP TYPE IF EXISTS feature_toggle_enum")
