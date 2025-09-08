
from OpenGL.GL import*

class ShaderClass:
    def __init__ (self, vertexFilePath, fragmentFilePath):
        self.__vertexShaderSource   = self.__LoadShaderSource (vertexFilePath  )
        self.__fragmentShaderSource = self.__LoadShaderSource (fragmentFilePath)

        self.__vertexShader = glCreateShader (GL_VERTEX_SHADER)
        glShaderSource  (self.__vertexShader, self.__vertexShaderSource  )
        glCompileShader (self.__vertexShader  )

        self.__fragmentShader =glCreateShader (GL_FRAGMENT_SHADER)
        glShaderSource  (self.__fragmentShader, self.__fragmentShaderSource)
        glCompileShader (self.__fragmentShader)

        if not glGetShaderiv (self.__vertexShader,   GL_COMPILE_STATUS):
            print ("ERROR: VERTEX SHADER (COMPILATION)\n")
            print (glGetShaderInfoLog (self.__vertexShader  ).decode ())

        if not glGetShaderiv (self.__fragmentShader, GL_COMPILE_STATUS):
            print ("ERROR: FRAGMENT SHADER (COMPILATION)\n")
            print (glGetShaderInfoLog (self.__fragmentShader).decode ())

        self.__shaderProgram = glCreateProgram ()
        glAttachShader (self.__shaderProgram, self.__vertexShader  )
        glAttachShader (self.__shaderProgram, self.__fragmentShader)
        glLinkProgram  (self.__shaderProgram)

        if not glGetProgramiv (self.__shaderProgram, GL_LINK_STATUS):
            print ("ERROR: SHADER PROGRAM (LINKING)\n")
            print (glGetProgramInfoLog (self.__shaderProgram).decode ())

        glDeleteShader  (self.__vertexShader  )
        glDeleteShader  (self.__fragmentShader)
    def CleanUp            (self):
        glDeleteProgram (self.__shaderProgram)

    def Use                (self):
        glUseProgram    (self.__shaderProgram)

    def SetUniformInteger  (self, name, value):
        location = glGetUniformLocation (self.__shaderProgram, name)
        if name == -1:
            print ("WARNING: UNIFORM INTEGER")
            print (name)
        else:
            glUniform1i (location, value)
            
    def __LoadShaderSource (self, filePath):
        with open (filePath, 'r') as shaderSource:
            return shaderSource.read ()
        