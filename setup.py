from setuptools import setup
 
# download_url='https://github.com/RDCH106/parallel_foreach_submodule/archive/v0.1.tar.gz', # Te lo explico a continuación
setup(
    name='ojitos369_mysql_db',
    packages=['ojitos369_mysql_db'], # Mismo nombre que en la estructura de carpetas de arriba
    include_package_data=True,
    version='1.0',
    license='LGPL v3', # La licencia que tenga tu paquete
    description='Funciones con conexiones a bases de datos',
    long_description='Funciones de utilidades de ojitos369\nRevizar README en:\nhttps://github.com/Ojitos369/ojitos369-pip',
    author='Ojitos369',
    author_email='ojitos369@gmail.com',
    url='https://github.com/Ojitos369/ojitos369-pip', # Usa la URL del repositorio de GitHub
    keywords='Utilidades de ojitos369', # Palabras que definan tu paquete
    install_requires=[
        'pymysql',
        'ojitos369'
    ],
    classifiers=[
        'Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
"""
# pip install setuptools twine
py3 setup.py sdist
twine upload dist/*
"""