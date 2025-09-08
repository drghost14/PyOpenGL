
import pygame
import sys
import numpy as np
import ctypes
from   OpenGL.GL import*
from   pyglm import glm

from engine.graphicsPipeline.shaderClass import ShaderClass
from engine.graphicsPipeline.vaoClass    import VaoClass
from engine.graphicsPipeline.bufferClass import BufferClass

from engine.textureClass                 import TextureClass
from engine.textureClass                 import TextureParameter

class GameClass:
    def __init__  (self):
        ctypes.windll.user32.SetProcessDPIAware () # DPI correction

        pygame.init ()
        pygame.display.gl_set_attribute (pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute (pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute (pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        self.__WIDTH  = 800
        self.__HEIGHT = 600
        self.__screen = pygame.display.set_mode ((self.__WIDTH, self.__HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)

        glEnable    (GL_BLEND)
        glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        self.__vertex = np.array ([
            -0.5, -0.5,     0.0, 0.0, # bottom left
             0.5, -0.5,     1.0, 0.0, # bottom right
             0.5,  0.5,     1.0, 1.0, # top right
            -0.5,  0.5,     0.0, 1.0  # top left
        ], dtype = np.float32)

        self.__index  = np.array ([
            0, 1, 2,
            0, 2, 3
        ], dtype = np.uint32)

        self.__shader = ShaderClass ("engine/shaders/vertex.glsl", "engine/shaders/fragment.glsl")

        self.__vao    = VaoClass    ()
        self.__vao.Bind             ()

        self.__vbo    = BufferClass (GL_ARRAY_BUFFER,         self.__vertex)
        self.__ebo    = BufferClass (GL_ELEMENT_ARRAY_BUFFER, self.__index )
        stride        = self.__vertex.itemsize * 4
        self.__vao.SetData          (0, 2, stride, ctypes.c_voidp (0)    )
        self.__vao.SetData          (1, 2, stride, ctypes.c_voidp (2 * self.__vertex.itemsize))
        self.__vao.Unbind           ()
        self.__run    = True

        self.__soldier = TextureClass ("data/s1.png", 0, TextureParameter.TEXTURE_NEAREST)
    def __CleanUp (self):
        self.__shader.CleanUp ()
        self.__vao   .CleanUp ()
        self.__vbo   .CleanUp ()
        self.__ebo   .CleanUp ()

        pygame.quit ()
        sys.exit    ()

    def Run       (self):
        while self.__run:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    self.__run = 0
            self.__Update ()
            self.__Draw   ()
            pygame.display.flip ()
        self.__CleanUp    ()

    def __Update  (self):
        pass
    def __Draw    (self):
        glClearColor       (245/255.0, 245/255.0, 250/255.0, 1.0)
        glClear            (GL_COLOR_BUFFER_BIT)

        self.__shader .Use               ()
        self.__soldier.Bind              ()
        self.__shader .SetUniformInteger ("uTexture", 0)
        self.__vao    .Bind              ()
        glDrawElements                   (GL_TRIANGLES, 6, GL_UNSIGNED_INT, ctypes.c_void_p (0))
        self.__vao    .Unbind            ()