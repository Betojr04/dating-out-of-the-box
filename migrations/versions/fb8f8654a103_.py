"""empty message

Revision ID: fb8f8654a103
Revises: f0ed019aa2e4
Create Date: 2023-02-15 22:57:39.855720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb8f8654a103'
down_revision = 'f0ed019aa2e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user__review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payload', sa.String(length=250), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.alter_column('groups_guidelines',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=250),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('groups_guidelines',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.drop_column('user_id')
        batch_op.drop_column('name')

    op.drop_table('user__review')
    op.drop_table('messages')
    # ### end Alembic commands ###