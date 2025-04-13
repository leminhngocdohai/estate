{
    'name': "estate",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': "",
    'author': "Lee",
    'website': "https://www.ntq-solution.com.vn",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',

        #last
        'views/estate_menus.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

