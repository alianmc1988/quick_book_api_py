"""Initial Migration

Revision ID: 34e1a42f110a
Revises:
Create Date: 2025-03-04 23:58:02.380830

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "34e1a42f110a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "businesses",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("address", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "type",
            postgresql.ENUM("BAR", "HOTEL", "RESTAURANT", name="business_type_enum"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("isActive", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("phone", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("other_phone", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "deleted_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.PrimaryKeyConstraint("id", name="businesses_pkey"),
        sa.UniqueConstraint("email", name="businesses_email_key"),
        sa.UniqueConstraint("other_phone", name="businesses_other_phone_key"),
        sa.UniqueConstraint("phone", name="businesses_phone_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_businesses_id", "businesses", ["id"], unique=False)
    op.create_table(
        "business_social_medias",
        sa.Column(
            "type",
            postgresql.ENUM(
                "FACEBOOK",
                "INSTAGRAM",
                "TWITTER",
                "TIKTOK",
                name="business_social_media_enum",
            ),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("profile", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("business_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
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
            name="business_social_medias_business_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id", name="business_social_medias_pkey"),
    )
    op.create_index(
        "ix_business_social_medias_id", "business_social_medias", ["id"], unique=False
    )
    op.create_table(
        "users",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "deleted_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.UniqueConstraint("email", name="users_email_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.create_table(
        "roles",
        sa.Column("role", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("user_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column("business_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
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
            name="roles_business_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="roles_user_id_fkey", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name="roles_pkey"),
        sa.UniqueConstraint(
            "business_id", "user_id", "role", name="roles_business_id_user_id_role_key"
        ),
    )
    op.create_index("ix_roles_id", "roles", ["id"], unique=False)
    op.create_table(
        "spaces",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "type",
            postgresql.ENUM("TABLE", "BEDROOM", "CHAIR", name="space_type_enum"),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("isActive", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("capacity", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("business_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "deleted_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.CheckConstraint(
            "capacity > 1 AND capacity < 20000", name="check_capacity_range"
        ),
        sa.CheckConstraint(
            "char_length(description) <= 250", name="check_description_length"
        ),
        sa.ForeignKeyConstraint(
            ["business_id"],
            ["businesses.id"],
            name="spaces_business_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="spaces_pkey"),
        sa.UniqueConstraint("name", "business_id", name="spaces_name_business_id_key"),
    )
    op.create_index("ix_spaces_id", "spaces", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_spaces_id", table_name="spaces")
    op.drop_table("spaces")
    op.drop_index("ix_roles_id", table_name="roles")
    op.drop_table("roles")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")
    op.drop_index("ix_business_social_medias_id", table_name="business_social_medias")
    op.drop_table("business_social_medias")
    op.drop_index("ix_businesses_id", table_name="businesses")
    op.drop_table("businesses")
    # Drop enum types
    op.execute("DROP TYPE IF EXISTS business_type_enum")
    op.execute("DROP TYPE IF EXISTS business_social_media_enum")
    op.execute("DROP TYPE IF EXISTS space_type_enum")
