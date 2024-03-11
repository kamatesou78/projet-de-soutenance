def calculer_engrenage(self):
    

	A_P = int(self.lineEdit_2_alpha.text())
	M = float(self.lineEdit_12_module.text())    
	Z1 = int(self.lineEdit_7_Z1.text())
	Z2 = int(self.lineEdit_22_Z2.text()) 
	A_H = float(self.lineEdit_beta.text())
	                
	U = Z2 / Z1
	i = float(Z1 / Z2)
	Cosinus1 = math.cos(math.radians(A_P))
	Cosinus2 = math.cos(math.radians(A_H))
	Cosinus3 = math.cos(math.radians(A_P_A_degre))
	Sinus1 = math.sin(math.radians(A_H))

	A_P_A = math.atan(math.tan(math.radians(A_P))/math.cos(math.radians(A_H)))
	A_P_A_degre = math.degrees(A_P_A)

	Mt = M / Cosinus2
	d1 = Z1*Mt
	d2 = Z2*Mt
	d1 = int(d1)
	d2 = int(d2)

	da1 = float(d1-2*M) 
	da2 = float(d2-2*M)

	df1 = float(d1+2.5*M) 
	df2 = float(d2+2.5*M)

	db1 = d1*Cosinus3
	db2 = d2*Cosinus3

	at11 = math.acos(db1/da1)
	at1 = math.degrees(at11)

	at22 = math.acos(db2/da2)
	at2 = math.degrees(at22)

	B = math.atan(math.tan(A_H)*math.cos(A_P_A))
	A_H_B = math.degrees(B)

	A_H_C_T1 = math.degrees(math.atan((da1/d1)*math.tan(A_H)))
	A_H_C_T2 = math.degrees(math.atan((da2/d2)*math.tan(A_H)))

	pn = math.pi * M

	pt = math.pi * Mt

	pbn = pn * Cosinus1

	pbt = pt * Cosinus3

	px = pn / Sinus1

	pz = Z1 * px

	b = 2 * px

	a = ((d2 - d1) / 2)

	Ha = M

	Hf = 1.25 * M

	h = Ha + Hf


