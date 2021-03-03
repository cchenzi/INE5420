import pathlib
from PyQt5 import QtGui, QtCore

from wireframe import Wireframe

class ObjLoader:

    def __init__(self, file_path):
        self.vertices = []
        self.mtl = None
        self.mtl_dict = {}
        self.mtl_parsing = ''
        self.obj_parsing = ''
        self.wireframes = []
        self.wireframe_index = 0
        self.load(file_path)

    def vertice_handler(self, args):
        x = float(args[0])
        y = float(args[1])
        z = float(args[2])
        vertex = (x, y, z)
        self.vertices.append(vertex)
    
    def mtllib_handler(self, args):
        file = args[0]
        file_path = str(pathlib.Path().absolute() / 'obj' / file)
        self.parse_file(file_path, self.mtl_parser)
    
    def usemtl_handler(self, args):
        mtl = args[0]
        self.mtl = self.mtl_dict[mtl]
    
    def object_name_handler(self, args):
        name = args[0]
        self.obj_parsing = name
    
    def object_build_handler(self, args):
        points = []
        for vertex in args:
            index = int(vertex) - 1
            points.append(self.vertices[index])
        print(f'AAAAACVVV: {points}')
        if not self.mtl:
            self.mtl = QtCore.Qt.black
        wireframe = Wireframe(points, self.wireframe_index, self.mtl)
        wireframe.name = self.obj_parsing
        self.wireframes.append(wireframe)
        self.wireframe_index += 1
        self.mtl = None
        self.obj_parsing = ''
    
    obj_parser = {
        'v': vertice_handler,
        'mtllib': mtllib_handler,
        'usemtl': usemtl_handler,
        'o': object_name_handler,
        'w': object_build_handler,
        'p': object_build_handler,
        'l': object_build_handler,
        'f': object_build_handler
    }
    
    def newmtl_handler(self, args):
        self.mtl_parsing = args[0]
    
    def Kd_handler(self, args):
        r = int(float(args[0]) * 255)
        g = int(float(args[1]) * 255)
        b = int(float(args[2]) * 255)
        color = QtGui.QColor(r, g, b)
        self.mtl_dict[self.mtl_parsing] = color
        self.mtl_parsing = ''

    mtl_parser = {
        'newmtl': newmtl_handler,
        'Kd': Kd_handler
    }


    def load(self, file_path):
        self.parse_file(file_path, self.obj_parser)
        print(self.wireframes)
        print('AAAAAAAAAAAAAAAA')
        print(self.vertices)
        
        
    def parse_file(self, file_path, parse_dict):
        with open(file_path) as file:
            for line in file.readlines():
                split = line.split()
                try:
                    statement = split[0]
                    args = split[1:]
                    parse_dict[statement](self, args)
                except IndexError:
                    # blank line
                    pass


def save():
    print('salva')
    pass