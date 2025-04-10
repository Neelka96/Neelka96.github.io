# Import Dependencies
from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Create ORM base class
class Base(DeclarativeBase):
    pass


class User(Base):
    # Table name
    __tablename__ = 'user'

    # Columns
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(unique = True, nullable = False)
    name: Mapped[str] = mapped_column(nullable = False)
    email: Mapped[str] = mapped_column(nullable = False)
    location: Mapped[str] = mapped_column(nullable = True)
    bio: Mapped[str] = mapped_column(nullable = True)
    
    # Relationship to repositories: back_populates ensures bidirectional linkage
    repositories: Mapped[list['Repository']] = relationship(back_populates='user')

    def __repr__(self):
        return f'<UserTable(id={self.id}, username={self.username})>'


class Repository(Base):
    # Table name
    __tablename__ = 'repositories'

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    
    # Relationships
    user: Mapped[User] = relationship(back_populates='repositories')
    languages: Mapped[list['RepoLanguage']] = relationship(back_populates='repository')
    
    def __repr__(self):
        return f'<Repository(id={self.id}, name={self.name})>'


# Main Table (Restaurant)
class Language(Base):
    # Table name
    __tablename__ = 'languages'

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # Relationships
    repos: Mapped[list['RepoLanguage']] = relationship(back_populates='language')
    
    def __repr__(self):
        return f'<Language(id={self.id}, name={self.name})>'


class RepoLanguage(Base):
    # Tablename
    __tablename__ = 'repo_languages'

    # Columns
    repo_id: Mapped[int] = mapped_column(ForeignKey('repositories.id'), primary_key=True)
    language_id: Mapped[int] = mapped_column(ForeignKey('languages.id'), primary_key=True)
    lines_of_code: Mapped[float] = mapped_column(Numeric(14, 2))
    
    # Relationships
    repository: Mapped['Repository'] = relationship(back_populates='languages')
    language: Mapped['Language'] = relationship(back_populates='repos')
    
    def __repr__(self):
        return f'<RepoLanguage(repo_id={self.repo_id}, language_id={self.language_id})>'



# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')