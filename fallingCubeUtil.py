import importlib
import maya.cmds as cmds
import maya.OpenMayaUI as omui

# import UI หลัก
import fallingCube.FallingCubeUI as FallingCubeUI
importlib.reload(FallingCubeUI)

def showUI():
    try:
        FallingCubeUI.ui.close()
        FallingCubeUI.ui.deleteLater()
    except:
        pass

    ui = FallingCubeUI.run()
    return ui
