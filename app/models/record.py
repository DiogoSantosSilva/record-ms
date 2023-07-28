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
    data = Column(String, nullable=True)
    fl_active = Column(Boolean, default=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())


class RecordSchemaInput(BaseModel):
    user_id: int
    titulo: str
    mensagem: str
    topico: str
    tag: str
    data: str
    tipo_registro: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class RecordSchemaOutput(BaseModel):
    id: int = None
    user_id: int = None
    titulo: str = None
    mensagem: str = None
    topico: str = None
    tag: str = None
    data: str = None
    tipo_registro: str = None
    fl_active: bool = False

    class Config:
        orm_mode = True
