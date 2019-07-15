import maya.OpenMaya as om
import maya.cmds as cm

def GETPOINTS_DB(geo):

	sel = om.MSelectionList()
	dag = om.MDagPath()

	sel.add(geo)
	sel.getDagPath(0,dag)

	mesh = om.MFnMesh(dag)

	vts=om.MFloatPointArray()
	mesh.getPoints(vts, om.MSpace.kWorld)

	return mesh,vts

def SETPOINTS_DB(geo, finalPos):	
	geo.setPoints(finalPos, om.MSpace.kWorld)
    
def VTX_COPY_POSITION_DB():
	listSel = cm.ls(sl=True, fl=True)

	#store the vert positions for each mesh
	mFnMesh, mesh1Vts = GETPOINTS_DB(listSel[0])
	mFnMeshTarget, mesh2Vts = GETPOINTS_DB(listSel[1])

	#set the points from mesh 1 to mesh 2
	SETPOINTS_DB(mFnMeshTarget,mesh1Vts)

VTX_COPY_POSITION_DB()