from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, DateTime, func

from app import Base


class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    titulo = Column(String)
    mensagem = Column(String)
    topico = Column(String)
    tag = Column(String)
    tipo_registro = Column(String)
    fl_active = Column(Boolean, default=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())


class RecordSchemaInput(BaseModel):
    user_id: int
    titulo: str
    mensagem: str
    topico: str
    tag: str
    tipo_registro: str


class RecordSchemaOutput(BaseModel):
    id: int
    user_id: int
    titulo: str
    mensagem: str
    topico: str
    tag: str
    tipo_registro: str
    fl_active: bool
    created: str
    updated: str
