select
    table_catalog,
    table_schema,
    table_name,
    column_name,
    case
        when udt_name='bpchar' then 'bpchar'||'('||character_maximum_length||')'
        when udt_name='varchar' then 'varchar'||'('||coalesce(character_maximum_length::text, 'max')||')'
        else udt_name
    end data_type,
    ordinal_position,
    is_nullable
from
    information_schema.columns
where
	table_schema not in ('information_schema', 'pg_catalog')
order by
    table_catalog,
    table_schema,
    table_name,
    ordinal_position;