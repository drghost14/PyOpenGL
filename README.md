## 🎨 PyOpenGL + Pygame — OOP VBO/EBO Rectangle Demo

This project is the **first episode** of a tutorial series that blends **Pygame** and **PyOpenGL** to teach modern graphics programming in Python.  
We kick things off by rendering a rectangle using **Vertex Buffer Objects (VBOs)** and **Element Buffer Objects (EBOs)** — all wrapped in a clean **Object-Oriented** architecture.


---

## 🚀 Features
- **Object-Oriented Design** — Reusable and modular `Rectangle` class.
- **Modern OpenGL** with VBOs & EBOs.
- **Pygame Integration** — Simple windowing and event loop.
- **Shader-Based Rendering** — Custom vertex and fragment shaders.
- Fully open-source with the **MIT License**.

---
## ⚡ Quick Start
```bash
git clone https://github.com/dr.ghost14/PyOpenGL.git
cd PyOpenGL
python main.py
```

## 📂 Project Structure
```
project/
│── main.py               # Entry point
│── engine/
│   ├── GraphicsPipeline/
│   │   ├── shaderClass.py
│   │   ├── vaoClass.py
│   │   └── fragment_shader.glsl
│   ├── shaders/
│   │   ├── vertex.glsl
│   │   └── fragment.glsl
│   ├── gameClass.py
│── README.md
└── LICENSE
```

---

## 📦 Requirements
- Python 3.10+
- `pygame`
- `PyOpenGL`
- `numpy`
- `pyglm`

Install dependencies:
```bash
pip install pygame PyOpenGL PyOpenGL_accelerate pyglm numpy
```

---

## 🖥️ Running the Program
```bash
python main.py
```
A window should appear displaying your first **indexed-rendered rectangle**.

---

## 📚 Learning Outcomes
By following this tutorial, you'll learn:
- The difference between **VBO** and **EBO**.
- How to pass vertex attributes to shaders.
- The basics of Pygame + OpenGL integration.
- How to keep code modular and scalable.

---
