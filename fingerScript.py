import maya.cmds as cm
import maya.mel as mel

axisL = ("X","Y","Z")


def FINGER_IK_CREATE_DB(void):
	cm.select(hi=1)
	listSel = cm.ls(sl=1,fl=1)
	listIK1 = []
	listIK2 = []
	listBind = []
	nF = cm.textField(nameF,tx=1,q=1)
	ikCtrl = "{}IK_ctrl".format(nF)
	ctrlLoc = "{}_srtDriven".format(nF)
	ctrlBuffer = "{}_srtBuffer".format(nF)
	ikHandle = '{}_ikHandle'.format(nF)
	pvLoc = "{}_pV".format(nF)
	revFinger = "rev_{}".format(nF)
	locPosFinger = "position_{}".format(nF)
	mD_fingers = "mD_curl_{}".format(nF)
	mD_fingers2 = "{}_02".format(mD_fingers)
	
	crvNum = len(listSel)

	for i in range(len(listSel)):
		cm.rename(listSel[i],"bn_{}IK_0{}".format(nF,i+1))
		listIK1.append("bn_{}IK_0{}".format(nF,i+1))

	cm.duplicate(listIK1[0],rc=1)

	cm.select(hi=1)
	listSel = cm.ls(sl=1,fl=1)

	for i in range(len(listSel)):
		cm.rename(listSel[i],"bn_{}FK_0{}".format(nF,i+1))
		listIK2.append("bn_{}FK_0{}".format(nF,i+1))

	cm.select(listIK1[0])
	cm.duplicate(rc=1)

	cm.select(hi=1)
	listSel = cm.ls(sl=1,fl=1)

	for i in range(len(listSel)):
		cm.rename(listSel[i],"bnb_{}_0{}".format(nF,i+1))
		cm.orientConstraint("bn_{}IK_0{}".format(nF,i+1),"bnb_{}_0{}".format(nF,i+1),mo=0)
		cm.orientConstraint("bn_{}FK_0{}".format(nF,i+1),"bnb_{}_0{}".format(nF,i+1),mo=0)
		listBind.append("bnb_{}_0{}".format(nF,i+1))

	cm.ikHandle( n=ikHandle, sj=listIK1[0], ee=listIK1[-1] )

	
	mel.eval('curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
	cm.rename("aaaa")
	cm.rename("aaaa",ikCtrl)
	cm.group(n=ctrlBuffer,em=1)
	cm.spaceLocator(n=ctrlLoc)
	cm.parent(ikCtrl,ctrlLoc)
	cm.parent(ctrlLoc,ctrlBuffer)
	parCon = cm.parentConstraint(listIK1[-1],ctrlBuffer)
	cm.delete(parCon)
	oriCon = cm.orientConstraint(listIK1[-2],ctrlBuffer)
	cm.delete(oriCon)
	cm.parent(ikHandle,ikCtrl)
	cm.spaceLocator(n=pvLoc)
	parCon = cm.pointConstraint(listIK1[-1],pvLoc)
	cm.delete(parCon)
	cm.parent(pvLoc,ikCtrl)
	cm.setAttr("{}.ty".format(pvLoc),-5)
	cm.setAttr("{}.tx".format(pvLoc),-5)
	cm.poleVectorConstraint( pvLoc, ikHandle )

	cm.addAttr(pvLoc,ln='ikFkBlend',at='double',min=0,max=1,dv=0,keyable=1)
	cm.addAttr(pvLoc,ln='curl',at='double',min=-10,max=10,dv=0,keyable=1)
	cm.shadingNode( "reverse",au = 1,n = revFinger )
	cm.connectAttr("{}.ikFkBlend".format(pvLoc),"{}.inputX".format(revFinger))

	for i in range(len(listIK1)-1):
		ctrlfk = "{}_0{}_ctrl".format(nF,i+1)
		locfk = "{}_0{}_srtDriven".format(nF,i+1)
		bufferfk = "{}_0{}_srtBuffer".format(nF,i+1)
		ctrlfkBack = "{}_0{}_ctrl".format(nF,i)

		cm.circle(n=ctrlfk,nr=(0,1,0),ch=0)
		cm.rotate(0,0,90,ctrlfk)
		cm.makeIdentity(a=1,r=1)
		mel.eval("select -r {0}.cv[0] {0}.cv[2] {0}.cv[4] {0}.cv[6];scale -r -ocp 1.5 1 1.5 ;".format(ctrlfk))
		cm.group(n=bufferfk,em=1)
		cm.spaceLocator(n=locfk)
		cm.parent(ctrlfk,locfk)
		cm.parent(locfk,bufferfk)
		parCon = cm.parentConstraint(listIK2[i],bufferfk)
		cm.delete(parCon)
		cm.orientConstraint(ctrlfk,listIK2[i])
		cm.connectAttr("{}.ikFkBlend".format(pvLoc),"{}_orientConstraint1.{}W1".format(listBind[i],listIK2[i]))
		cm.connectAttr("{}.outputX".format(revFinger),"{}_orientConstraint1.{}W0".format(listBind[i],listIK1[i]))

		if (i != 0):
			cm.parent(bufferfk,ctrlfkBack)

	cm.spaceLocator(n=locPosFinger)
	poiCon = cm.pointConstraint(listIK1[0],locPosFinger)
	cm.delete(poiCon)
	cm.pointConstraint(locPosFinger,listIK1[0])
	cm.pointConstraint(locPosFinger,listIK2[0])
	cm.pointConstraint(locPosFinger,listBind[0])
	cm.pointConstraint(locPosFinger,"{}_01_srtBuffer".format(nF))
	cm.connectAttr("{}.ikFkBlend".format(pvLoc),"{}_01_srtBuffer.v".format(nF))
	cm.connectAttr("{}.outputX".format(revFinger),"{}.v".format(ctrlBuffer))

	cm.shadingNode( "multiplyDivide",au = 1,n = mD_fingers )

	if(len(listIK1)-1 > 3):
		cm.shadingNode( "multiplyDivide",au = 1,n = mD_fingers2 )

	for i in range(len(listIK1)-1):
		cm.addAttr(pvLoc,ln="_0{}".format(i+1),at='double',min=0,max=10,dv=10,keyable=1)

		if(i <= 2):
			cm.connectAttr( "{}._0{}".format(pvLoc,i+1),"{}.input1{}".format(mD_fingers,axisL[i]) )
			cm.connectAttr( "{}.curl".format(pvLoc),"{}.input2{}".format(mD_fingers,axisL[i]) )
			cm.connectAttr( "{}.output{}".format(mD_fingers,axisL[i]),"{}_0{}_srtDriven.rx".format(nF,i+1) )

		if(i > 2):
			cm.connectAttr( "{}._0{}".format(pvLoc,i+1),"{}.input1{}".format(mD_fingers2,axisL[i-3]) )
			cm.connectAttr( "{}.curl".format(pvLoc),"{}.input2{}".format(mD_fingers2,axisL[i-3]) )
			cm.connectAttr( "{}.output{}".format(mD_fingers2,axisL[i-3]),"{}_0{}_srtDriven.rx".format(nF,i+1) )
	

#-------------------------------------WINDOW-------------------------------------
if cm.window('fingerIK_window',exists=1):
	cm.deleteUI('fingerIK_window')

fingerIK_w = cm.window('fingerIK_window',t='fingerIK')
mainWindow = cm.columnLayout(adj=3)
cm.separator(h=10,style='none')
cm.text('name')
nameF = cm.textField()
cm.separator(h=10,style='none')
cm.button(l='CREATE',c=FINGER_IK_CREATE_DB,h=40)




cm.showWindow(fingerIK_w)