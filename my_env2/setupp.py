from setuptools import setup
setup(
    name="odoo",
    version="0.1",
    description="Este es un paquete para pruebas en Odoo",
    author="Luis Merino",
    author_email="luisfmerinot@gmail.com",
    url="http://brianda.es",
    packages=['odoo','odoo.addons','odoo.addons.tarea5'],
    scripts=[]
)
#python setup.py sdist
#luis@msilfmt:~/enviroments/my_env/dist$ pip install pruebas-0.1.tar.gz
#pip3 list
