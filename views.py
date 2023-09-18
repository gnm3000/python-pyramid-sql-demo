from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.orm import sessionmaker
from models import Customer  
from sqlalchemy import create_engine, text
import random
import string

engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

@view_config(route_name='generic_query', renderer='templates/generic_query.mako')
def generic_query(request):
    table = request.matchdict.get('table')
    field = request.matchdict.get('field')
    value = request.matchdict.get('value')
    connection = engine.connect()
    sql_query = text("SELECT * FROM " + table + " WHERE " + field + " = '" + value + "'")
    print("SQL Query:", sql_query)
    result = connection.execute(sql_query)
    field_names = list(result.keys())
    print("field_names", field_names)
    data = result.fetchall()
    html = '<body><h1>Customer List</h1>'
    html += '<ul></ul></body>'
    return {"data": data, "field_names": field_names, "table": table}

@view_config(route_name='customer_info', renderer='templates/customer_info.mako')
def customer_info(request):
    field = request.matchdict.get('field')
    value = request.matchdict.get('value')
    Session = sessionmaker(bind=engine)
    session = Session()
    customers = session.query(Customer).filter_by(**{field: value}).all()
    html = '<body><h1>Customer List</h1>'
    html += '<ul>'
    for customer in customers:
        html += f'<li>{customer.FirstName} {customer.LastName} - {customer.Country}</li>'
    html += '</ul></body>'
    return {'result': html}

