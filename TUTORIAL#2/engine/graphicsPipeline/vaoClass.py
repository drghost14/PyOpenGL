
from OpenGL.GL import*

class VaoClass:
    def __init__ (self):
        self.__vao = glGenVertexArrays (1)
        if self.__vao == 0: # vao correction
            print ("ERROR: VAO (GENERATION)\n")
    def CleanUp  (self):
        self.Bind            ()
        glDeleteVertexArrays (1, [int (self.__vao)])

    def Bind     (self):
        glBindVertexArray    (self.__vao)
    def Unbind   (self):
        glBindVertexArray    (0)
    
    def SetData  (self, index, size, stride, pointer):
        glVertexAttribPointer     (index, size, GL_FLOAT, GL_FALSE, stride, pointer)
        glEnableVertexAttribArray (index)
