import maya.cmds as cmds
import sys
sys.path.append("D:\\akshay\\script")
import gearClassCreator

class BaseWindow(object):

    windowName = "BaseWindow"

    def show(self):

        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName)
        self.buildUI()
        cmds.showWindow()


    def buildUI(self):
        column = cmds.columnLayout()
        cmds.text(label="this is base window")
        cmds.setParent(column)

        cmds.button(label="Close", command=self.close)
        print"hello"



    def reset(self,*args):
        pass

    def close(self,*args):
        cmds.deleteUI(self.windowName)

class GearUI(BaseWindow):
    windowName="gearWindow"


    def __init__(self):
        self.gear = None

    def buildUI(self):

        column = cmds.columnLayout()
        cmds.text(label="Use the slider to change the gear")

        row = cmds.rowLayout(numberOfColumns=4)
        self.label = cmds.text(label="10")
        self.slider=cmds.intSlider(min=3, max=30, value=10, step=1, dragCommand = self.modifyGear)
        cmds.button(label="Make Gear", command=self.makeGear)
        cmds.button(label="Reset", command=self.reset)


        cmds.setParent(column)
        cmds.button(label="Close", command=self.close)


    def makeGear(self,*args):
        side= cmds.intSlider(self.slider, query=True, value=True)
        self.gear = gearClassCreator.Gear()
        self.gear.createGear(teeth=side)



    def modifyGear(self,teeth):
        if self.gear:
            self.gear.changeTeeth(teeth=teeth)

        cmds.text(self.label, edit=True, label=teeth)

    def reset(self, *args):
        self.gear = None
        cmds.intSlider(self.slider, edit=True, value=10)
        cmds.text(self.label, edit=True, label=10)