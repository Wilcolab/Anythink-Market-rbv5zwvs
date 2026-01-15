"""add is_verified column to users

Revision ID: c3e1af192159
Revises: fdf8821871d7
Create Date: 2026-01-15 00:00:00.000000

"""
import sqlalchemy as sa
from alembic import op

revision = "c3e1af192159"
down_revision = "fdf8821871d7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("is_verified", sa.Boolean, nullable=False, server_default=sa.false()))


def downgrade() -> None:
    op.drop_column("users", "is_verified")