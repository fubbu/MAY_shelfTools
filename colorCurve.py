import maya.cmds as cmds

def COLOR_SHAPE_CHANGE_DB(void):
	color = cmds.intField(colorNumb,v=1,q=1)
	#---------------------------------------------------------

	listSel = cmds.ls(sl=1,fl=1)

	for item in listSel:
		listShape = cmds.listRelatives(item, type="shape", f=True)
		for shapes in listShape:
			cmds.setAttr("{}.overrideEnabled".format(shapes), True)
			cmds.setAttr("{}.overrideColor".format(shapes), color)

#-------------------------------------WINDOW-------------------------------------
if cmds.window('Color_Shape',exists=1):
	cmds.deleteUI('Color_Shape')

Color_Shape = cmds.window('Color_Shape',t='Color Shape')
mainWindow = cmds.columnLayout(adj=3)
cmds.separator(h=10,style='none')
cmds.text('color number')
colorNumb = cmds.intField()
cmds.separator(h=10,style='none')
cmds.button(l='CHANGE',c=COLOR_SHAPE_CHANGE_DB,h=40)

cmds.showWindow(Color_Shape)