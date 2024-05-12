'''Start a data analytics project.'''
import pathlib

def create_project_directory(directory_name: str): 
    '''
    Creates a project sub-directory.
    :param directory_name: Name of the directory to be created, e.g. "test"
    '''
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main(): 
    ''' Scaffold a project. '''
    create_project_directory(directory_name='test') 
    create_project_directory(directory_name='docs') 

if __name__ == '__main__':
    main()