from copy import copy
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from app.db.database import Base
from app.configuration.config import Settings


def create_record(db: Session, db_class: Base, record: any):
    _record = db_class(**record.__dict__)
    db.add(_record)
    db.commit()
    db.refresh(_record)
    return _record


def update_record(
    db: Session,
    db_class: Base,
    where: dict,
    new: dict,
):
    update_query = filter_stmt(update(db_class), where, db_class)
    db.execute(update_query.values(**new))
    db.commit()
    return read_record(db, where, db_class)


def delete_record(
    db: Session,
    db_class: Base,
    where: dict,
):
    record = copy(read_record(db, where, db_class))
    delete_query = filter_stmt(delete(db_class), where, db_class)
    db.execute(delete_query)
    db.commit()
    return record


def filter_stmt(stmt: any, where: dict, db_class: Base):
    for field, value in where.items():
        stmt = stmt.filter(getattr(db_class, field) == value)
    return stmt


def read_record(db: Session, where: dict, db_class: Base):
    result = db.execute(filter_stmt(select(db_class), where, db_class)).first()
    return result[0] if result else None


def query(db: Session, selectable):
    return db.execute(selectable).scalars().all()


def query_one(db: Session, selectable):
    return db.execute(selectable).first()


def create_many(db: Session, model_class, records):
    try:
        db.bulk_insert_mappings(model_class, records)
        db.commit()
        return True
    except Exception as e:
        Settings().error_logger.error(f"{e}")
        db.rollback()
        return False


def update_many(db: Session, model_class, records):
    try:
        db.bulk_update_mappings(model_class, records)
        db.commit()
        return True
    except Exception as e:
        Settings().error_logger.error(f"{e}")
        db.rollback()
        return False
