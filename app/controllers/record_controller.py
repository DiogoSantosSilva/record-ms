from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.record import RecordSchemaInput, RecordSchemaOutput
from app.services.record_service import RecordService
from app import get_db

router = APIRouter(prefix="/records", tags=["records"])


@router.get("/", response_model=List[RecordSchemaOutput])
def get_all_records(user_id: int = None, db: Session = Depends(get_db)):
    record_service = RecordService(db)
    db_records = record_service.get_records(user_id)
    return db_records


@router.post("/", response_model=RecordSchemaOutput)
def create_record(record: RecordSchemaInput, db: Session = Depends(get_db)):
    record_service = RecordService(db)
    db_record = record_service.create_record(record)
    return db_record


@router.get("/{record_id}", response_model=RecordSchemaOutput)
def get_record_by_id(record_id: int, db: Session = Depends(get_db)):
    record_service = RecordService(db)
    db_record = record_service.get_record(record_id)
    return db_record


@router.put("/{record_id}", response_model=RecordSchemaOutput)
def update_record_by_id(record_id: int, record: RecordSchemaInput, db: Session = Depends(get_db)):
    record_service = RecordService(db)
    db_record = record_service.update_record(record_id, record)
    return db_record


@router.delete("/{record_id}")
def delete_record_by_id(record_id: int, db: Session = Depends(get_db)):
    record_service = RecordService(db)
    return record_service.delete_record(record_id)
