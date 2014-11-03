bl_info = {
  "name": "Run IPython in terminal",
  "author": "Gabriel Montagné",
  "warning": "You should be running Blender with IPython in your python path.",
  "category": "Development",
}

import bpy

def register():
    print('Register IPython addon')

def unregister():
    print('Unregister run IPython addon')

if __name__ == '__main__':
    register()
