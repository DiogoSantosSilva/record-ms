from typing import Optional, List

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.models.record import Record, RecordSchemaInput


class RecordService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_records(self, user_ids: Optional[List[int]] = None):
        query = self.db.query(Record)

        if user_ids is not None:
            query = query.filter(Record.user_id.in_(user_ids))

        return query.all()

    def create_record(self, record):
        try:
            db_record = Record(**record.dict())
            self.db.add(db_record)
            self.db.commit()
            self.db.refresh(db_record)
            return db_record
        except SQLAlchemyError:
            self.db.rollback()
            raise
        except Exception:
            self.db.rollback()
            raise

    def get_record(self, record_id: int):
        return self.db.query(Record).filter(Record.id == record_id).first()

    def update_record(self, record_id: int, record: RecordSchemaInput):
        try:
            db_record = self.db.query(Record).filter(Record.id == record_id).one()
            db_record.user_id = record.user_id
            db_record.titulo = record.titulo
            db_record.mensagem = record.mensagem
            db_record.topico = record.topico
            db_record.tag = record.tag
            db_record.tipo_registro = record.tipo_registro
            self.db.commit()
            self.db.refresh(db_record)
            return db_record
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Record not found")
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")

    def delete_record(self, record_id: int) -> None:
        try:
            record = self.db.query(Record).filter(Record.id == record_id).one()
            self.db.delete(record)
            self.db.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Record not found")
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")
