# big-expectations
Great Expectations for BigQuery

# Requirements
- `python3-dev`

# Sample Usage

```
context = get_data_context('project-id', 'service-account-key.json')
ds = context.get_dataset('dataset.table_or_view')
print(ds._is_numeric_column('some_column'))
```
