
from OpenGL.GL import*

class BufferClass:
    def __init__ (self, target, data):
        self.__buffer = glGenBuffers            (1)
        glBindBuffer (target, self.__buffer       )
        glBufferData (target, data, GL_STATIC_DRAW)
    def CleanUp  (self):
        glDeleteBuffers (1, [int (self.__buffer)])
    
