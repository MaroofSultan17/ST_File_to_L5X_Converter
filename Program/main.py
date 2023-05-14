import argparse
import os
from xml.etree.ElementTree import Element, ElementTree, SubElement


def st_to_l5x(st_file_path, l5x_file_path):
    # Parse the ST file
    with open(st_file_path, 'r') as st_file:
        st_program = st_file.read()

    # Create the root element of the L5X file
    l5x_root = Element('RSLogix5000Content')

    # Create the Controller element
    controller = SubElement(l5x_root, 'Controller')
    controller.set('Name', 'MyController')

    # Create the Programs element
    programs = SubElement(controller, 'Programs')

    # Create the Program element
    program = SubElement(programs, 'Program')
    program.set('Name', 'MyProgram')

    # Create the Routines element
    routines = SubElement(program, 'Routines')

    # Create the Routine element
    routine = SubElement(routines, 'Routine')
    routine.set('Name', 'MainRoutine')

    # Create the ST code element and add it to the Routine element
    st_code = SubElement(routine, 'ST')
    st_code.text = st_program

    # Create the L5X file
    l5x_tree = ElementTree(l5x_root)
    l5x_tree.write(l5x_file_path)

    print(f'Successfully converted {st_file_path} to {l5x_file_path}')


if __name__ == '__main__':
    st_file = input("Enter the path of the ST file: ")
    l5x_file = input("Enter the path of the L5X file: ")
    st_file_path = st_file
    l5x_file_path = l5x_file
    # st_file_path = r'C:\Users\maroo\OneDrive\Desktop\Sir Abdul Khali\st.ST'
    # l5x_file_path = r'C:\Users\maroo\OneDrive\Desktop\Sir Abdul Khali\l5x.L5X'

    # Check that the ST file exists
    if not os.path.isfile(st_file_path):
        print(f'Error: {st_file_path} does not exist')
        exit()

    # Convert the ST file to L5X
    st_to_l5x(st_file_path, l5x_file_path)

    print("\n \n" + "Converted file is: " + "\n \n")
    # show the converted file in the console
    with open(l5x_file_path, 'r') as l5x_file:
        print(l5x_file.read())
