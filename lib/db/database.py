# Import dependencies
from contextlib import contextmanager
from collections.abc import Sequence, Generator
from sqlalchemy import create_engine, event, Engine, Select, Row
from sqlalchemy.orm import sessionmaker, Session as Session_Class
from sqlalchemy.sql import Executable

# Import configuration
from config import Config
config = Config()

# Create logger
import logging
log = logging.getLogger(__name__)

# Import protocols
from .protocols import DBAPI_Connection


# Single engine instance for class blueprint
engine = create_engine(config.ENGINE_URI)

# Event listener for engine connection, enforces foreign keys upon connection
@event.listens_for(Engine, 'connect')
def enforce_sqlite_fks(dbapi: DBAPI_Connection, conn_record) -> None:
    cursor = dbapi.cursor()
    cursor.execute('PRAGMA foreign_keys=ON;')
    cursor.close()
    return None

# Bind session to engine now that modifications to engine are done
SessionLocal = sessionmaker(bind = engine, expire_on_commit = False)

# Composition based class definition
class Database:
    def __init__(self):
        self.__session = SessionLocal

    # Context management handler for sessions for centralized handling
    @contextmanager
    def get_session(self) -> Generator[Session_Class]:
        '''Custom session context manager for SQL Alchemy.

        Yields:
            Generator[SessionType]: New session from bound engine connection pool.
        '''
        session = self.__session()
        try:
            yield session
            session.commit()
            log.debug('Session successfully committed.')
        except Exception:
            session.rollback()
            log.critical('Session rollback from error.')
            raise 
        finally:
            session.close()
            log.debug('Closing session.')
            

    # Utility for executing session requests
    def execute_query(
            self
            ,stmt: Executable
            ,params: dict | Sequence[dict] | None = None
            ) -> Sequence[Row] | int:
        '''Wrapper for custom context manager for simple and bulk queries.

        Args:
            stmt (Executable): `Select`, `Insert`, `Delete`, and other Core `SQL` clause types.
            params (dict | Sequence[dict] | None, optional): Data or constraints to be used. Defaults to None.

        Returns:
            Sequence[Row]: Returns view of data from `Select` type.
            int: Non-select executable type returns 0.
        '''
        with self.get_session() as session:
            log.debug('execute_query() called.')
            try:
                result = session.execute(stmt, params) if params else session.execute(stmt)
                log.debug('execute_query() successfully utilized.')
                return result.scalars().all() if isinstance(stmt, Select) else 0
            except Exception:
                log.critical('Could not use BP reduced execute_query() function.')
                raise


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')