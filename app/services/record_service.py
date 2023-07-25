from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.models.record import Record, RecordSchemaInput


class RecordService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_records(self, user_id: Optional[int] = None):
        query = self.db.query(Record)
        if user_id is not None:
            query = query.filter(Record.user_id == user_id)
        return query.all()

    def create_record(self, record: RecordSchemaInput) -> RecordSchemaInput:
        try:
            self.db.add(record)
            self.db.commit()
            self.db.refresh(record)
            return record
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")

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
            return {"message": "Record updated successfully"}
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
