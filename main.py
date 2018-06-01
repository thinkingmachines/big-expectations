from sqlalchemy import create_engine
import great_expectations as ge

def get_data_context(uri, credentials_path):
    context = ge.get_data_context('SqlAlchemy', uri)
    context.engine = create_engine(uri, credentials_path=credentials_path)
    return context

dc = get_data_context('bigquery://level-4-yoga', 'key.json')
ds = dc.get_dataset('data_audit.sales_info_kpis')

def fullFn(ds):
    return {'success': True}

def mapFn(ds, column):
    print('\t\tds: {}'.format(ds))
    print('\t\tcolumn: {}'.format(column))
    return False

def aggFn(ds, column):
    print('\t\tds: {}'.format(ds))
    print('\t\tcolumn: {}'.format(column))
    return {
        'result': {'observed_value': 9000},
        'success': True
    }

# print('Results:')
# print('\t1: {}'.format(ds.test_expectation_function(fullFn)))
# print('\t2: {}'.format(ds.test_column_map_expectation_function(mapFn, column='AMEX')))
# print('\t3: {}'.format(ds.test_column_aggregate_expectation_function(aggFn, column='AMEX')))
