import maya.cmds as cmds

def AUTO_SAVE_PROJECT_DB(*args):
    filepath = cmds.file(q=True, sn=True)
    fileName = filepath.split("/")[-1]
    filepath = filepath.split("/")
    del filepath[-1]
    saveFolder = "/".join(filepath)
    fileName = fileName.split(".")[0]
    fileName = fileName.split("v")[-1]
    fileName = int(fileName)+1

    cmds.file(rename="{}/v{}.ma".format(saveFolder, str(fileName)))
    cmds.file(save=True, type="mayaAscii")

AUTO_SAVE_PROJECT_DB()