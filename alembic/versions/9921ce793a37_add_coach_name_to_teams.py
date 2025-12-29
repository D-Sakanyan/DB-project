"""add_coach_name_to_teams

Revision ID: 9921ce793a37
Revises: 
Create Date: 2025-12-29 16:46:49.935777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9921ce793a37'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('teams', sa.Column('coach_name', sa.String(), nullable=True))

def downgrade() -> None:
    op.drop_column('teams', 'coach_name')