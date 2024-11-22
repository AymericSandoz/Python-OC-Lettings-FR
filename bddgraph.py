from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'


# Création du diagramme E-A
diagram = Digraph('E-A Diagram', format='png')
diagram.attr(rankdir='LR', size='8,5')

# User
diagram.node('User', 'User\n(1:1 avec Profile)', shape='box')

# Profile
diagram.node('Profile', 'Profile\n- favorite_city', shape='ellipse')

# Address
diagram.node(
    'Address', 'Address\n- number\n- street\n- city\n- state\n- zip_code\n- country_iso_code', shape='ellipse')

# Letting
diagram.node('Letting', 'Letting\n- title', shape='ellipse')

# Relations
diagram.edge('User', 'Profile', label='1:1')
diagram.edge('Profile', 'User', label='1:1')
diagram.edge('Letting', 'Address', label='1:1')

# Rendu
file_path = "/mnt/data/diagram_ea_bdd"
diagram.render(file_path, cleanup=True)
file_path + ".png"
