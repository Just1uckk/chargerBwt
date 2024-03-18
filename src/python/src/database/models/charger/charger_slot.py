from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT

from database.models.base import Base
from database.models.mixins import MysqlTimestampsMixin, MysqlPrimaryKeyMixin


class ChargerSlot(
    Base,
    MysqlTimestampsMixin,
    MysqlPrimaryKeyMixin
):
    __tablename__ = 'charger_slots'

    number = Column("number", VARCHAR(255), nullable=False, index=True)
    address = Column("address", VARCHAR(255), nullable=False, index=False)
    api_address = Column("api_address", VARCHAR(255), nullable=False, index=True)
    price = Column("price", BIGINT(unsigned=True), nullable=False, index=True)
    status = Column("status", VARCHAR(255), nullable=False, index=True)
    type = Column("type", VARCHAR(255), nullable=False, index=True)
    sent_to_customer = Column("sent_to_customer", VARCHAR(255))
