from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '000001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # ### Create users table ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, unique=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True, server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # ### Create tokens table ###
    op.create_table(
        'tokens',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, unique=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('token', sa.String(), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now())
    )


def downgrade() -> None:
    # ### Drop tokens table ###
    op.drop_table('tokens')

    # ### Drop users table ###
    op.drop_table('users')
