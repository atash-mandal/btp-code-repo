import os

def get_design():
	design = f"""
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
try:
	oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
except:
	pass
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
	"""
	return design
	
def gap_script(y_cor,rect,max_width,cnt):
	x = -1.0 * (max_width/2.0)
	y_cor = y_cor*1000.0
	length = 1000.0*rect.d
	width = 1000.0*max_width
	height = 1000.0*rect.h
	max_width = max_width*1000.0

	gap_content = f"""
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x)+'mm'}",
		"YStart:="		, "{str(y_cor)+'mm'}",
		"ZStart:="		, "0mm",
		"Width:="		, "{str(max_width)+'mm'}",
		"Height:="		, "{str(length)+'mm'}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Ground'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "{str(x)+'mm'}",
		"YPosition:="		, "{str(y_cor)+'mm'}",
		"ZPosition:="		, "0mm",
		"XSize:="		, "{str(width)+'mm'}",
		"YSize:="		, "{str(length)+'mm'}",
		"ZSize:="		, "{str(height)+'mm'}"
	],
	[
		"NAME:Attributes",
		"Name:="		, "{'Substrate'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(238 247 251)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"FR4_epoxy\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	"""
	return gap_content 


def microstrip_script(y_cor,rect,max_width,cnt):
	x = -1000.0 * (max_width/2.0)
	y_cor = 1000.0*y_cor
	x_cor_strip = -1000.0*(rect.w/2.0)
	width = 1000.0*max_width
	line_width = 1000.0*rect.w
	length = 1000.0*rect.l
	height = 1000.0*rect.h
	microstrip_content = f"""
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x)+'mm'}",
		"YStart:="		, "{str(y_cor)+'mm'}",
		"ZStart:="		, "0mm",
		"Width:="		, "{str(width)+'mm'}",
		"Height:="		, "{str(length)+'mm'}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Ground'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "{str(x)+'mm'}",
		"YPosition:="		, "{str(y_cor)+'mm'}",
		"ZPosition:="		, "0mm",
		"XSize:="		, "{str(width)+'mm'}",
		"YSize:="		, "{str(length)+'mm'}",
		"ZSize:="		, "{str(height)+'mm'}"
	],
	[
		"NAME:Attributes",
		"Name:="		, "{'Substrate'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(189 189 175)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"FR4_epoxy\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x_cor_strip)+'mm'}",
		"YStart:="		, "{str(y_cor)+'mm'}",
		"ZStart:="		, "{str(height)+'mm'}",
		"Width:="		, "{str(line_width)+'mm'}",
		"Height:="		, "{str(length)+'mm'}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Strip'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	"""
	return microstrip_content


def stub_script(y_cor,rect,max_width,cnt):
	x = -1000.0 * (max_width/2.0)
	x_cor_strip =  -1000.0 * (rect.w/2.0)
	y_cor_strip = 1000.0*y_cor
	x_cor_stub = 1000.0*rect.w/2.0
	y_cor_stub = 1000.0*(y_cor + rect.l1)
	y_cor = 1000.0*y_cor
	max_width = 1000.0*max_width
	height = 1000.0*rect.h
	line_length = 1000.0*(rect.l1+rect.l2+rect.w0)
	line_width = 1000.0*rect.w
	stub_length = 1000.0*rect.l0
	stub_width = 1000.0*rect.w0
	stub_content = f"""
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x)+'mm'}",
		"YStart:="		, "{str(y_cor)+'mm'}",
		"ZStart:="		, "0mm",
		"Width:="		, "{str(max_width)+'mm'}",
		"Height:="		, "{str(line_length)+'mm'}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Ground'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "{str(x)+'mm'}",
		"YPosition:="		, "{str(y_cor)+'mm'}",
		"ZPosition:="		, "0mm",
		"XSize:="		, "{str(max_width)+'mm'}",
		"YSize:="		, "{str(line_length)+'mm'}",
		"ZSize:="		, "{str(height)+'mm'}"
	],
	[
		"NAME:Attributes",
		"Name:="		, "{'Substrate'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(189 189 175)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"FR4_epoxy\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x_cor_strip)+'mm'}",
		"YStart:="		, "{str(y_cor_strip)+'mm'}",
		"ZStart:="		, "{str(height)}mm",
		"Width:="		, "{str(line_width)+'mm'}",
		"Height:="		, "{str(line_length)+'mm'}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Strip'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x_cor_stub)+'mm'}",
		"YStart:="		, "{str(y_cor_stub)+'mm'}",
		"ZStart:="		, "{str(height)}mm",
		"Width:="		, "{str(stub_length)+'mm'}",
		"Height:="		, "{str(stub_width)+'mm'}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Stub'+str(cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "{'Strip'+str(cnt)},{'Stub'+str(cnt)}"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False,
		"TurnOnNBodyBoolean:="	, True
	])
	"""
	return stub_content


def port_script(x_cor,y_cor,x_size,z_size,port_cnt):
	line_x = 1000.0*(x_size/2.0 + x_cor)
	x_cor = 1000.0*x_cor
	y_cor = 1000.0*y_cor
	z_size = 1000.0*z_size
	x_size = 1000.0*x_size
	port_content = f"""
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{str(x_cor)+'mm'}",
		"YStart:="		, "{str(y_cor)+'mm'}",
		"ZStart:="		, "0mm",
		"Width:="		, "{str(z_size)+'mm'}",
		"Height:="		, "{str(x_size)+'mm'}",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{'Port'+str(port_cnt)}",
		"Flags:="		, "",
		"Color:="		, "(255 255 26)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oModule.AssignLumpedPort(
	[
		"NAME:{port_cnt}",
		"Objects:="		, ["{'Port'+str(port_cnt)}"],
		"LumpedPortType:="	, "Modal",
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Coordinate System:="	, "Global",
					"Start:="		, ["{line_x}mm","{y_cor}mm","0mm"],
					"End:="			, ["{line_x}mm","{y_cor}mm","{z_size}mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi"
			]
		],
		"Impedance:="		, "50ohm"
	])
	"""
	return port_content

def get_boundary_setup():
	setup = f"""
oModule = oDesign.GetModule("BoundarySetup")
"""
	return setup

def create_boundary(boundary_list):
	boundary = f"""
oModule.AssignPerfectE(
	[
		"NAME:PerfE1",
		"Objects:="		, {boundary_list},
		"InfGroundPlane:="	, False
	])
"""
	return boundary

def create_rad_box(x_size, y_size, z_size):
	rad_x = 5000.0 * x_size
	rad_y = 5000.0 * y_size
	rad_z = 5000.0 * z_size
	max_d = max({rad_x, rad_y, rad_z})
	radbox = f"""
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "{str(-1.0 * (max_d/2.0 - x_size/2.0))+'mm'}",
		"YPosition:="		, "{str(-1.0 * (max_d/2.0 - y_size/2.0))+'mm'}",
		"ZPosition:="		, "{str(-1.0 * (max_d/2.0 - z_size/2.0))+'mm'}",
		"XSize:="		, "{str(max_d)+'mm'}",
		"YSize:="		, "{str(max_d)+'mm'}",
		"ZSize:="		, "{str(max_d)+'mm'}"
	],
	[
		"NAME:Attributes",
		"Name:="		, "RadBox",
		"Flags:="		, "",
		"Color:="		, "(189 189 175)",
		"Transparency:="	, 1,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["RadBox"]
	])
"""
	return radbox


def create_modal_setup():
	analysis = f"""
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "5GHz",
		"MaxDeltaS:="		, 0.02,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 12,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"DrivenSolverType:="	, "Direct Solver",
		"EnhancedLowFreqAccuracy:=", False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced",
		"InfiniteSphereSetup:="	, "",
		"MaxPass:="		, 10,
		"MinPass:="		, 1,
		"MinConvPass:="		, 1,
		"PerError:="		, 1,
		"PerRefine:="		, 30
	])
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "0.1GHz",
		"RangeEnd:="		, "10GHz",
		"RangeCount:="		, 1000,
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False
	])
"""
	return analysis


def create_py_script(hfss_structures, file_name):
	downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")
	script_directory = downloads_directory+"\hfss_scripts"
	if not os.path.exists(script_directory):
		os.makedirs(script_directory)

	full_file_name = f"{script_directory}\{file_name}.py"

	with open(full_file_name, "w") as file:
		file.write("")
		file.flush()

	max_width = 0.0
	for rect in hfss_structures:
		if str(type(rect)) == "<class 'skmd.network.Network'>":
			return
		try:
			max_width = max(max_width, 1.2 * 2 * (rect.l0 + rect.w))
		except:
			try:
				max_width = max(max_width, 5 * rect.w)
			except:
				pass
	
	design = get_design()
	with open(full_file_name, "a") as file:
		file.write(design)
		file.flush()

	start_y = 0.0	
	cnt = 1
	for rect in hfss_structures:
		if str(type(rect)) == "<class 'skmd.structure.Microstripline'>":
			content = microstrip_script(start_y,rect,max_width,cnt)
		elif str(type(rect)) == "<class 'visualizer.network.Stub'>":
			content = stub_script(start_y,rect,max_width,cnt)
		else:
			content = gap_script(start_y,rect,max_width,cnt)

		with open(full_file_name, "a") as file:
			file.write(content)
			file.flush()
		try:
			start_y = start_y + rect.l
		except:
			try:
				start_y = start_y + rect.d
			except:
				start_y = start_y + rect.l1 + rect.l2 + rect.w0
		cnt = cnt + 1
	
	n = int(len(hfss_structures))
	port_1 = port_script(-1.0 * (hfss_structures[0].w/2.0),0,hfss_structures[0].w,hfss_structures[0].h,1)
	port_2 = port_script(-1.0 * (hfss_structures[n-1].w/2.0),start_y,hfss_structures[n-1].w,hfss_structures[n-1].h,2)

	bnd_cnt = 1
	boundary_list = "["
	for rect in hfss_structures:
		if str(type(rect)) == "<class 'skmd.structure.Microstripline'>":
			boundary_list = boundary_list + '\"' + str("Strip"+str(bnd_cnt)) + '\",'
			boundary_list = boundary_list + '\"' + str("Ground"+str(bnd_cnt)) + '\"'
		elif str(type(rect)) == "<class 'skmd.structure.Gap'>":
			boundary_list = boundary_list + '\"' + "Ground"+str(bnd_cnt) + '\"'
		else:
			boundary_list = boundary_list + '\"' + str("Strip"+str(bnd_cnt)) + '\",'
			boundary_list = boundary_list + '\"' + str("Ground"+str(bnd_cnt)) + '\"'
		boundary_list = boundary_list + ","
		bnd_cnt = bnd_cnt + 1
	boundary_list = boundary_list[:-1]
	boundary_list = boundary_list + "]"
	radbox = create_rad_box(max_width, start_y, hfss_structures[0].h)
	boundary = create_boundary(boundary_list)
	setup = get_boundary_setup()
	report = create_modal_setup()
	with open(full_file_name, "a") as file:
			file.write(setup)
			file.write(port_1)
			file.write(port_2)
			file.write(boundary)
			file.write(radbox)
			file.write(report)
			file.flush()

	print("done")


