from datetime import datetime
from typing import Dict

from commands.base_csv_exporter import BaseCSVExporter
from database.models.charger import ChargerSlot
from sqlalchemy.sql.base import Executable as SQLAlchemyExecutable
from sqlalchemy import update


class ConnectorExporterCommand(BaseCSVExporter):
    table = ChargerSlot
    file_extension = 'xlsx'

    def build_update_query_stmt(self, row: Dict) -> SQLAlchemyExecutable:
        export_date = {self.export_date_column: datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S.%fZ')}
        update_date_stmt = update(self.table).values(**export_date)
        return update_date_stmt.where(self.table.id == row['id'])
