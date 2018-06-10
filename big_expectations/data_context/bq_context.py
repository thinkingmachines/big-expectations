import great_expectations as ge
from sqlalchemy import create_engine

BQ_URI_FMT = 'bigquery://{}'

def get_data_context(project_id, credentials_path):
    uri = BQ_URI_FMT.format(project_id)
    context = ge.get_data_context('SqlAlchemy', uri)
    context.engine = create_engine(uri, credentials_path=credentials_path)
    return context
