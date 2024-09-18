{
    'name': 'Project Custom Payment',
    'version': '17.0',
    'summary': 'Custom enhancements for project payment management',
    'description': """
        This module provides custom enhancements to manage payment terms and status for project tasks.
    """,
    'author': 'Abdelwahab',
    'website': 'http://www.abdoelwahab.com',
    'category': 'Project Management',
    'depends': ['project'],
    'data': [
        'views/project_task_views.xml',
    ],
    'installable': True,
    'application': True,
}
