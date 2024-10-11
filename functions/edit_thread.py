import xml.etree.ElementTree as ET

def edit_threads(route_file, number_threads):
    # Cargar el archivo XML
    tree = ET.parse(route_file)
    root = tree.getroot()

    # Encontrar el nodo ThreadGroup
    for thread_group in root.iter('ThreadGroup'):
        for int_prop in thread_group.iter('intProp'):
            if int_prop.get('name') == 'ThreadGroup.num_threads':
                # Modificar el valor del número de hilos
                int_prop.text = str(number_threads)
                break

    # Guardar el archivo XML modificado
    tree.write(route_file, encoding='UTF-8', xml_declaration=True)