import maya.cmds as cm

def CONNECTION_TRANSLATE_DB(void):
	axis = cm.textField(translateCon,tx=1,q=1)
	#---------------------------------------------------------

	listAxis = list(axis)
	listSelection = cm.ls( sl=1,fl=1 )
	connectedFrom = listSelection[0]
	listSelection.remove(connectedFrom)

	for i in range(len(listSelection)):
		if "x" in listAxis:
			cm.connectAttr( "{}.tx".format(connectedFrom),"{}.tx".format(listSelection[i]) )
		if "y" in listAxis:
			cm.connectAttr( "{}.ty".format(connectedFrom),"{}.ty".format(listSelection[i]) )
		if "z" in listAxis:
			cm.connectAttr( "{}.tz".format(connectedFrom),"{}.tz".format(listSelection[i]) )


def CONNECTION_ROTATE_DB(void):
	axis = cm.textField(rotateCon,tx=1,q=1)
	#---------------------------------------------------------

	listAxis = list(axis)
	listSelection = cm.ls( sl=1,fl=1 )
	connectedFrom = listSelection[0]
	listSelection.remove(connectedFrom)

	for i in range(len(listSelection)):
		if "x" in listAxis:
			cm.connectAttr( "{}.rx".format(connectedFrom),"{}.rx".format(listSelection[i]) )
		if "y" in listAxis:
			cm.connectAttr( "{}.ry".format(connectedFrom),"{}.ry".format(listSelection[i]) )
		if "z" in listAxis:
			cm.connectAttr( "{}.rz".format(connectedFrom),"{}.rz".format(listSelection[i]) )


def CONNECTION_SCALE_DB(void):
	axis = cm.textField(scaleCon,tx=1,q=1)
	#---------------------------------------------------------

	listAxis = list(axis)
	listSelection = cm.ls( sl=1,fl=1 )
	connectedFrom = listSelection[0]
	listSelection.remove(connectedFrom)

	for i in range(len(listSelection)):
		if "x" in listAxis:
			cm.connectAttr( "{}.sx".format(connectedFrom),"{}.sx".format(listSelection[i]) )
		if "y" in listAxis:
			cm.connectAttr( "{}.sy".format(connectedFrom),"{}.sy".format(listSelection[i]) )
		if "z" in listAxis:
			cm.connectAttr( "{}.sz".format(connectedFrom),"{}.sz".format(listSelection[i]) )





#-------------------------------------WINDOW-------------------------------------
if cm.window('Connection_Window',exists=1):
	cm.deleteUI('Connection_Window')

Connection_Window = cm.window('Connection_Window',t='Connection Window')
mainWindow = cm.columnLayout(adj=3)
cm.separator(h=10,style='none')
cm.text('Connection axis')
translateCon = cm.textField(it = "xyz")
cm.separator(h=10,style='none')
cm.button(l='TRANSLATE',c=CONNECTION_TRANSLATE_DB,h=40)
cm.separator(h=20,style='none')
cm.text('Connection axis')
rotateCon = cm.textField(it = "xyz")
cm.separator(h=10,style='none')
cm.button(l='ROTATE',c=CONNECTION_ROTATE_DB,h=40)
cm.separator(h=20,style='none')
cm.text('Connection axis')
scaleCon = cm.textField(it = "xyz")
cm.separator(h=10,style='none')
cm.button(l='SCALE',c=CONNECTION_SCALE_DB,h=40)



cm.showWindow(Connection_Window)