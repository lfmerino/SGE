# -*- coding: utf-8 -*-
# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK
contenido1="""<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>
	<id>tag:mail.google.com,2008:filters:z0000001595174856075*7938583813627151337,z0000001595174897582*1746739103250145449</id>
	<updated>2021-01-03T18:59:45Z</updated>
	<author>
		<name>luisfrancisco.merino Brianda</name>
		<email>lmerino@coitt.es</email>
	</author>"""

with open('mi_fichero.xml', 'w') as f2:
    f2.write(contenido1)
#f2.close()
contenido1="""	<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001595174856075*7938583813627151337</id>
		<updated>2021-01-03T18:59:45Z</updated>
		<content></content>
		<apps:property name='from' value='"""
contenido2="""'/>
		<apps:property name='label' value='Revisar'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>
    """
with open('direcciones.txt', 'r') as f1:
    for linea in f1:
        with open('mi_fichero.xml', 'a') as f2:
            f2.write(contenido1+linea[:-1]+contenido2)
        print(linea[:-1])
with open('mi_fichero.xml', 'a') as f2:
    f2.write('</feed>\n')
        

