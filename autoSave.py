import maya.cmds as cmds

filepath = cmds.file(q=True, sn=True)
filepath = filepath.split("/")[-1]
filepath = filepath.split(".")[0]
filepath = filepath.split("v")[-1]
filepath = int(filepath)+1

cmds.file(rename="v{}.ma".format(str(filepath)))
cmds.file(save=True, type="mayaAscii")