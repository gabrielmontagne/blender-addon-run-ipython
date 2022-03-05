bl_info = {
  "name": "Run IPython in console",
  "author": "Gabriel Montagné Láscaris-Comneno",
  "warning": "You should be running Blender with IPython in your Python path."
              "Blender won't redraw until you're done!",
  "category": "Development",
  "blender": (2, 80, 0)
}

import bpy
from bpy.props import IntProperty, FloatProperty, StringProperty, BoolProperty

class RunIPythonOperator(bpy.types.Operator):
    """Run IPython Operator"""
    bl_idname = "run_ipython.run"
    bl_label = "Run IPython in console"

    reduce_logging: BoolProperty(default=True, name='ears')

    def execute(self, context):
        try:
            import IPython
            import logging

            if self.reduce_logging:
                print('reduce logging')
                logging.getLogger().setLevel(logging.ERROR)

            IPython.embed()
        except:
            self.report({'ERROR'}, "Couldn't import IPython")
            return {'CANCELLED'}
        else:
            return {'FINISHED'}

def register():
    bpy.utils.register_class(RunIPythonOperator)

def unregister():
    print('Unregister run IPython addon')

if __name__ == '__main__':
    register()
