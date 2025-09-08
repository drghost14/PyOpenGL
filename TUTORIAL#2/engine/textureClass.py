
import pygame
from   enum import Enum, IntEnum
from   OpenGL.GL import*

class TextureParameter (Enum):
    TEXTURE_LINEAR  = 1
    TEXTURE_NEAREST = 2

class TextureClass:
    def __init__ (self, filePath, textureUnit, textureParam):
        self.__textureID        = glGenTextures (1)
        self.__textureUnit      = textureUnit
        self.__textureParameter = textureParam
        self.__texture          = pygame.image.load (filePath).convert_alpha () # for invisible background

        imageData               = pygame.image.tostring (self.__texture, "RGBA", True)
        width, height           = self.__texture.get_size ()

        glActiveTexture (self.__textureUnit + GL_TEXTURE0)
        glBindTexture   (GL_TEXTURE_2D, self.__textureID )

        match self.__textureParameter:
            case TextureParameter.TEXTURE_LINEAR :
                glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
                glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

            case TextureParameter.TEXTURE_NEAREST:
                glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST)
                glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glTexImage2D     (GL_TEXTURE_2D, 0, GL_RGBA, width, height, 
                      0, GL_RGBA, GL_UNSIGNED_BYTE, imageData)
        glGenerateMipmap (GL_TEXTURE_2D)
        glBindTexture    (GL_TEXTURE_2D, self.__textureID)

    def Bind (self):
        glActiveTexture (self.__textureUnit + GL_TEXTURE0)
        glBindTexture   (GL_TEXTURE_2D, self.__textureID)
