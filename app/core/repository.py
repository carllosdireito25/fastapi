from sqlalchemy.orm import Session

from app.core.database import SessionLocal


class Repository:
    _db: Session

    def save(self, model) -> None:
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)

    def close(self) -> None:
        self._db.close()

    def set_db(self, session_local: SessionLocal) -> None:
        self._db = session_local

def get_repository():
    try:
        repository = Repository()
        repository.set_db(SessionLocal())
        yield repository
    finally:
        repository.close()
