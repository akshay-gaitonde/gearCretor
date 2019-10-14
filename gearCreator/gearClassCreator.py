import maya.cmds as cmds

class Gear(object):

    """
    this is gear class to create the gear
    method used:
        createGear(self,teeth=10,length=0.3) with default values teeth and length
        changeTeeth(self, teeth=10, length=0.3) with default values teeth and length
    """
    def __init__(self):
        print "initializing gear object"
        self.transform= None
        self.constructor=None
        self.extrude=None

    def createGear(self,teeth=10,length=0.3):
        """
        this function is used to create gear with given number of teeth and length of it
        Args:
            teeth: give the number of teeth
            length: give the length of teeth

        Returns:
            self.transform
            self.constructor
            self.extrude

        """
        spans = teeth * 2

        self.transform, self.constructor = cmds.polyPipe(subdivisionsAxis=spans)

        sideFaces = range(spans * 2, spans * 3, 2)

        cmds.select(clear=True)
        for face in sideFaces:
            cmds.select('%s.f[%s]'%(self.transform, face),add=True)

        self.extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]





    def changeTeeth(self, teeth=10, length=0.3):
        """
        this function is used to change the number of teeth and its length
        Args:
            teeth: give the NEW number of teeth
            length: give the NEW length of teeth

        Returns:
            self.transform
            self.constructor
            self.extrude

        """

        # todo   if not extrude, constructor:
        #    raise RuntimeError(" either constructor or extrude node is deleted, maybe you have deleted construction history")

        # new number of  faces (spans)= teeth*2
        spans = teeth * 2

        # edit the gear
        cmds.polyPipe(self.constructor, edit=True, subdivisionsAxis=spans)

        # select the side faces of pipe
        sideFaces = range(spans * 2, spans * 3, 2)
        faceNames = []

        for face in sideFaces:
            fname = 'f[%s]' % (face)
            faceNames.append(fname)

        cmds.setAttr('%s.inputComponents' % (self.extrude), len(faceNames), *faceNames, type="componentList")

        cmds.polyExtrudeFacet(self.extrude, edit=True, localTranslateZ=length)