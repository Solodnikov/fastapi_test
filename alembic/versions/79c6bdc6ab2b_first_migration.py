"""First migration

Revision ID: 79c6bdc6ab2b
Revises: 
Create Date: 2025-02-24 17:39:03.324578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79c6bdc6ab2b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('referral_codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('expiration_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_referral_codes_code'), 'referral_codes', ['code'], unique=True)
    op.create_index(op.f('ix_referral_codes_id'), 'referral_codes', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('referral_code_id', sa.Integer(), nullable=True),
    sa.Column('referrer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['referral_code_id'], ['referral_codes.id'], ),
    sa.ForeignKeyConstraint(['referrer_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_referral_codes_id'), table_name='referral_codes')
    op.drop_index(op.f('ix_referral_codes_code'), table_name='referral_codes')
    op.drop_table('referral_codes')
    # ### end Alembic commands ###
