from setuptools import setup
setup(
    name="odoo",
    version="0.5",
    description="Paquete de pruebas para odoo",
    author="Luis Merino",
    author_email="luisfmerinot@gmail.com",
    url="briandademendoza.es",
#    packages=['odoo','odoo.addons','odoo.addons.tarea5','odoo.addons.tarea5.modPasswd','odoo.addons.tarea5.modUsuario','odoo.addons.tarea5.modTabla','odoo.addons.tarea5.mismodulos','odoo.addons.julio.p123','odoo.addons.julio.p4','odoo.addons.julio.p5','odoo.addons.julio.p6','odoo.addons.mismodulos'],
    packages=['odoo','odoo.addons','odoo.addons.tarea5','odoo.addons.tarea5.modPasswd','odoo.addons.tarea5.modUsuario',
	'odoo.addons.tarea5.modTabla','odoo.addons.tarea5.mismodulos','odoo.addons.mismodulos','sge05'
	,'sge05.ejercicio1','sge05.ejercicio2','sge05.ejercicio3'
	,'sge05.ejercicio4','sge05.ejercicio5','sge05.ejercicio6'
	,'sge05.utilidades'],
    scripts=[]
)
