import maya.cmds as cm

def COLOR_SHAPE_CHANGE_DB(void):
	color = cm.intField(colorNumb,v=1,q=1)
	#---------------------------------------------------------

	listSel = cm.ls(sl=1,fl=1)

	for i in range(len(listSel)):
		listShape = cm.listRelatives( listSel[i],c=1 )
		cm.setAttr( "{}.overrideEnabled".format(listShape[0]),1 )
		cm.setAttr( "{}.overrideColor".format(listShape[0]),color )

#-------------------------------------WINDOW-------------------------------------
if cm.window('Color_Shape',exists=1):
	cm.deleteUI('Color_Shape')

Color_Shape = cm.window('Color_Shape',t='Color Shape')
mainWindow = cm.columnLayout(adj=3)
cm.separator(h=10,style='none')
cm.text('color number')
colorNumb = cm.intField()
cm.separator(h=10,style='none')
cm.button(l='CHANGE',c=COLOR_SHAPE_CHANGE_DB,h=40)

cm.showWindow(Color_Shape)