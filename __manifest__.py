{
    'name': 'Customer Request',
    'version': '16.0.1.0',
    
    'summary': 'Manage Customer',
    'description': 'Module quản lý khách hàng',
    'author': 'Bach Bui',
   
    'depends': [
        'crm',
        'product',
        'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_request_views.xml',
        'views/crm_lead_views.xml',
       
    ],
  'installable': True,
'application': True,
}