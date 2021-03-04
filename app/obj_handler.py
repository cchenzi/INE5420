import pathlib
from PyQt5 import QtGui, QtCore

from app.wireframe import Wireframe


class ObjLoader:
    def __init__(
        self, file_path, wireframe_index, normalization_values, window_transformations
    ):
        self.vertices = []
        self.mtl = None
        self.mtl_dict = {}
        self.mtl_parsing = ""
        self.obj_parsing = ""
        self.wireframes = []
        self.wireframe_index = wireframe_index
        self.normalization_values = normalization_values
        self.window_transformations = window_transformations
        self.load(file_path)

    def vertice_handler(self, args):
        x = float(args[0])
        y = float(args[1])
        # z = float(args[2])
        vertex = (x, y)
        self.vertices.append(vertex)

    def mtllib_handler(self, args):
        file = args[0]
        file_path = str(pathlib.Path().absolute() / "obj" / file)
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
            if vertex[0] == "-":
                index = int(vertex)
                points.append(self.vertices[index])
            else:
                index = int(vertex) - 1
                points.append(self.vertices[index])
        if not self.mtl:
            self.mtl = QtCore.Qt.black
        wireframe = Wireframe(
            points,
            self.wireframe_index,
            self.mtl,
            self.normalization_values,
            self.window_transformations,
        )
        wireframe.name = self.obj_parsing
        print(wireframe.name)
        self.wireframes.append(wireframe)
        self.wireframe_index += 1
        self.mtl = None
        self.obj_parsing = ""

    obj_parser = {
        "v": vertice_handler,
        "mtllib": mtllib_handler,
        "usemtl": usemtl_handler,
        "o": object_name_handler,
        "w": object_build_handler,
        "p": object_build_handler,
        "l": object_build_handler,
        "f": object_build_handler,
    }

    def newmtl_handler(self, args):
        self.mtl_parsing = args[0]

    def Kd_handler(self, args):
        r = int(float(args[0]) * 255)
        g = int(float(args[1]) * 255)
        b = int(float(args[2]) * 255)
        color = QtGui.QColor(r, g, b)
        self.mtl_dict[self.mtl_parsing] = color
        self.mtl_parsing = ""

    mtl_parser = {"newmtl": newmtl_handler, "Kd": Kd_handler}

    def load(self, file_path):
        self.parse_file(file_path, self.obj_parser)

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


class ObjWriter:
    def __init__(self, wireframes_list, scene_name, desnormalization_matrix):
        self.wirefames_list = wireframes_list
        self.scene_name = scene_name
        self.desnormalization_matrix = desnormalization_matrix
        print(self.desnormalization_matrix)

    def create_obj(self):
        obj_lines = []
        mtl_lines = []
        obj_lines.append(f"mtllib {self.scene_name}.mtl\n")

        for wireframe in self.wirefames_list:
            obj_list, mtl_list = wireframe.to_obj(self.desnormalization_matrix)
            obj_lines += obj_list
            mtl_lines += mtl_list

        file_path = str(pathlib.Path().absolute() / "obj" / self.scene_name)
        obj_name = file_path + ".obj"
        mtl_name = file_path + ".mtl"
        self.write_file(obj_name, obj_lines)
        self.write_file(mtl_name, mtl_lines)

    def write_file(self, file_name, lines):
        with open(file_name, "w") as writer:
            for line in lines:
                writer.write(line)
