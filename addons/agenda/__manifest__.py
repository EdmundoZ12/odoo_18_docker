# -*- coding: utf-8 -*-
{
    "name": "Agenda",
    "summary": "Modulo de anuncios academicos emulando una agenda escolar",
    "description": """
        Modulo con el proposito de enviar anuncios, eventos y en general notificaciones a usuarios de un colegio; Padres, Alumnos, Administrativos y Profesores
    """,
    "author": "Grupo 28 - Software 1",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Productivity",
    "version": "0.1",
    "installable": True,
    "auto_install": False,
    "application": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "hr", "mail"],
    # always loaded
    # añadir las vistas que vayan a agregar el ORDEN IMPORTAAA CARGAR EN JERARQUIA
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        
        'data/agenda_data.xml',
        'views/agenda_profesores.xml',
        'views/agenda_administrativos.xml',
        'views/agenda_tutores.xml',
        'views/agenda_alumnos.xml',
        'views/agenda_materias.xml',
        'views/agenda_cursos.xml',
        'views/agenda_publicaciones.xml',
        'views/agenda_tipopublicaciones.xml',

        'views/agenda_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/demo_materia.xml',
        'demo/demo_curso.xml',
        'demo/demo_administrativo.xml',
        'demo/demo_profesor.xml',
        'demo/demo_tutor.xml',
        'demo/demo_alumno.xml',
        'demo/demo_cursoalumno.xml',
        'demo/demo_profesorcurso.xml',
        'demo/demo_tipopublicacion.xml',
        'demo/demo_publicacion.xml',
    ],
}
