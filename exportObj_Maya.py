from __future__ import print_function
from string import join
import maya.cmds as cm
import os
import maya.mel as mel


def EXPORT_OBJ_FIX_DB(*args):
	nameFolder = cm.textField(groupName, tx=True, q=True)
	USERPROFILE = os.path.expandvars( '$USERPROFILE' )
	USERPROFILE = USERPROFILE.replace('\\','/')
	USERPROFILE = "{}/Desktop/{}".format(USERPROFILE,nameFolder)

	exportGroupFolder_DB = []
	exportGroupFolderHierarchy_DB = []

	cm.select(hi=True)
	listSel = cm.ls(sl=True, fl=True, type='transform')

	for item in listSel:
		listRel = cm.listRelatives(item, type='shape')
		if not listRel == None:
			exportGroupFolder_DB.append(item)

	cm.select(exportGroupFolder_DB)

	listSel = cm.ls(sl=True, fl=True, l=True, type='transform')

	for item in listSel:
		dirSplit = item.split('|')
		dirReplace = []
		for i in range(len(dirSplit)-1):
			dirReplace.append(dirSplit[i])
			dirCheck = '/'.join(dirReplace)
			if not os.path.isdir('{}{}'.format(USERPROFILE,dirCheck)):
				os.makedirs('{}{}'.format(USERPROFILE,dirCheck))

		dirReplace = '/'.join(dirReplace)
		cm.select(item)
		mel.eval('file -force -options "groups=0;ptgroups=0;materials=0;smoothing=0;normals=0" -typ "OBJexport" -pr -es "{}{}/{}.obj";'.format(USERPROFILE,dirReplace,dirSplit[-1]))
		print ("{}{}/{}.obj".format(USERPROFILE,dirReplace,dirSplit[-1]),file = open('{}/importSort'.format(USERPROFILE),'a'))

def IMPORT_OBJ_FIX_DB(*args):
	nameFolder = cm.textField(groupName, tx=True, q=True)
	USERPROFILE = os.path.expandvars( '$USERPROFILE' )
	USERPROFILE = USERPROFILE.replace('\\','/')
	USERPROFILE = "{}/Desktop/{}".format(USERPROFILE,nameFolder)

	for line in open('{}/importSort'.format(USERPROFILE),'r'):
		line = line.rstrip()
		name = line.split('/')
		name = name[-1][:-4]
		if not line:
			continue
		folder = line.replace(USERPROFILE,"")
		folder = folder.split('/')
		folder = folder[1:]
		if not "obj" in folder[0]:
			for i in range(len(folder)):
				if not "obj" in folder[i]:
					if not cm.objExists(folder[i]):
						cm.group(n=folder[i],em=True)
						if folder[i] != folder[0]:
							cm.parent(folder[i],folder[i-1])
			mel.eval('file -import -type "OBJ"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace "importFile" -options "mo=1"  -pr  -importTimeRange "combine" "{}";'.format(line))
			cm.select("importFile:Mesh")
			RENAME_IMPORT_DB(name)
			
			cm.parent(name,folder[-2])

def RENAME_IMPORT_DB(i_name):
	cm.rename("aaaa")
	cm.rename("aaaa", i_name)

#-------------------------------------WINDOW-------------------------------------
if cm.window('importOBJ_window',exists=1):
	cm.deleteUI('importOBJ_window')

window = cm.window('importOBJ_window',t='import obj')
cm.columnLayout()
groupName = cm.textField(w=300,h=25)
cm.separator(h=10,style='none')
cm.button(l='EXPORT',c=EXPORT_OBJ_FIX_DB,h=40,w=300)
cm.separator(h=10,style='none')
cm.button(l='IMPORT',c=IMPORT_OBJ_FIX_DB,h=40,w=300)
cm.showWindow( window )