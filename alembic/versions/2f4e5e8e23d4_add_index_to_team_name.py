"""add_index_to_team_name

Revision ID: 2f4e5e8e23d4
Revises: 9921ce793a37
Create Date: 2025-12-29 16:55:36.608849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f4e5e8e23d4'
down_revision: Union[str, Sequence[str], None] = '9921ce793a37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_index('ix_teams_name', 'teams', ['name'])

def downgrade() -> None:
   op.drop_index('ix_teams_name', 'teams')