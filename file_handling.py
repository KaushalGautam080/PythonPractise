



# def read_file():
#     filename = '/Users/kaushal-vt/Downloads/IMG_5663.JPG'
#     try:
#         file = open(filename,'r')
#         content = file.read
#         print(content.__name__)

#     except Exception as e:
#         print(f"Unable to read file due to following exception:${e}")
#     finally:
#         file.close()
        
        



def read_file_with():
    filename = '/Users/kaushal-vt/Downloads/IMG_5663.JPG'
    
    with open(filename,'rb') as file:
        content = file.read()
        print(content)
        
    
read_file_with()


    
class FileManager:
    def __enter__():
        yield
        
    def __exit__():
        raise
    

with FileManager:
    print(1)
    
    
from contextlib import contextmanager
@contextmanager
def open_file():
    try:
     yield
    
        
    finally:
        print("always executed")