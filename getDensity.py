def getDensity(h):
	# Returns International Standard Atmosphere 1976 density as a function
	# of height in meters
	# https://en.wikipedia.org/wiki/Barometric_formula#Density_equations
	R_star = 8.3144598
	g0     = 9.80665
	M      = 0.0289644
	if h < 11000:
		hb   = 0
		rhob = 1.225
		Tb   = 288.15
		Lb   = -0.0065
		rho = rhob * ( Tb / ( Tb + Lb*(h - hb) ) )**( 1 + ( g0 * M / (R_star * Lb)))
	elif h < 20000:
		hb   = 11000
		rhob = 0.36391
		Tb   = 216.65
		rho = rhob * math.exp( -g0 * M * (h - hb)/(R_star * Tb) )
	elif h < 32000:
		hb   = 20000
		rhob = 0.08803
		Tb   = 216.65
		Lb   = 0.001
		rho = rhob * ( Tb / ( Tb + Lb*(h-hb) ) )**( 1 + ( g0 * M / (R_star * Lb)))
	elif h < 47000:
		hb   = 32000
		rhob = 0.01322
		Tb   = 228.65
		Lb   = 0.0028
		rho = rhob * ( Tb / ( Tb + Lb*(h-hb) ) )**( 1 + ( g0 * M / (R_star * Lb)))
	elif h < 51000:
		hb   = 47000
		rhob = 0.00143
		Tb   = 270.65
		rho = rhob * math.exp( -g0 * M * (h - hb)/(R_star * Tb) )
	elif h < 71000:
		hb   = 51000
		rhob = 0.00086
		Tb   = 270.65
		Lb   = -0.0028
		rho = rhob * ( Tb / ( Tb + Lb*(h-hb) ) )**( 1 + ( g0 * M / (R_star * Lb)))
	elif h < 84852:
		hb   = 71000
		rhob = 0.000064
		Tb   = 214.65
		Lb   = -0.002
		rho = rhob * ( Tb / ( Tb + Lb*(h-hb) ) )**( 1 + ( g0 * M / (R_star * Lb)))
	else:
		rho = 0
	return rho
