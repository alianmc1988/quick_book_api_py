from typing import Sequence, Union

from alembic import op

"""remove hotels from types

Revision ID: 8a9ab85c5759
Revises: 06b4a66127e9
Create Date: 2025-03-07 12:59:44.523062

"""

# revision identifiers, used by Alembic.
revision: str = "8a9ab85c5759"
down_revision: Union[str, None] = "06b4a66127e9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE business_type_enum RENAME TO business_type_enum_old")
    op.execute("CREATE TYPE business_type_enum AS ENUM('BAR', 'RESTAURANT')")
    op.execute(
        "ALTER TABLE businesses ALTER COLUMN type TYPE business_type_enum "
        "USING type::text::business_type_enum"
    )
    op.execute("DROP TYPE business_type_enum_old")
    op.execute("ALTER TYPE space_type_enum RENAME TO space_type_enum_old")
    op.execute("CREATE TYPE space_type_enum AS ENUM('TABLE', 'CHAIR')")
    op.execute(
        "ALTER TABLE spaces ALTER COLUMN type TYPE space_type_enum "
        "USING type::text::space_type_enum"
    )
    op.execute("DROP TYPE space_type_enum_old")


def downgrade() -> None:
    op.execute("ALTER TYPE business_type_enum RENAME TO business_type_enum_old")
    op.execute("CREATE TYPE business_type_enum AS ENUM('BAR', 'HOTEL', 'RESTAURANT')")
    op.execute(
        "ALTER TABLE businesses ALTER COLUMN type TYPE business_type_enum "
        "USING type::text::business_type_enum"
    )
    op.execute("DROP TYPE business_type_enum_old")
    op.execute("ALTER TYPE space_type_enum RENAME TO space_type_enum_old")
    op.execute("CREATE TYPE space_type_enum AS ENUM('TABLE', 'BEDROOM', 'CHAIR')")
    op.execute(
        "ALTER TABLE spaces ALTER COLUMN type TYPE space_type_enum "
        "USING type::text::space_type_enum"
    )
    op.execute("DROP TYPE space_type_enum_old")
