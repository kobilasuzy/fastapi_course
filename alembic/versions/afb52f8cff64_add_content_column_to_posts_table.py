"""add content column to posts table

Revision ID: afb52f8cff64
Revises: c93bd8e4c718
Create Date: 2024-01-29 11:18:39.065827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afb52f8cff64'
down_revision = 'c93bd8e4c718'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
