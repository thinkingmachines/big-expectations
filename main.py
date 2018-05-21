import great_expectations as ge
from sqlalchemy import create_engine

def get_data_context(uri, credentials_path):
    context = ge.get_data_context('SqlAlchemy', uri)
    context.engine = create_engine(uri, credentials_path=credentials_path)
    return context
