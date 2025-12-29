"""add_result_score_difference

Revision ID: ca6df04e1a5d
Revises: 2f4e5e8e23d4
Create Date: 2025-12-29 19:04:44.962152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca6df04e1a5d'
down_revision: Union[str, Sequence[str], None] = '2f4e5e8e23d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('results', sa.Column('score_difference', sa.Integer(), nullable=True))
    op.create_index('ix_results_score_difference', 'results', ['score_difference'])

def downgrade() -> None:
    op.drop_index('ix_results_score_difference', 'results')
    op.drop_column('results', 'score_difference')