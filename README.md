# MKS-MFC-647C

This is an example of source code using python programming language to control MKS instrument multi gas controller type 647C 
In the manual provided by MKS instrument, chapter 4 instructs as well as list the necessary command syntax.

FS c xxxx      enter setpoint of a channel
 c = 1..4         channel 
 x = 0..1100      setpoint in 0.1 percent of full scale 

RA c rr 	enter range
 c = 1..4	  channel
 r = 0..39   range code:

 		0 = 1.000 SCCM, 20 = 1.000 SCFH
		1 = 2.000 SCCM, 21 = 2.000 SCFH
 		2 = 5.000 SCCM, 22 = 5.000 SCFH
 		3 = 10.00 SCCM, 23 = 10.00 SCFH
 		4 = 20.00 SCCM, 24 = 20.00 SCFH
 		5 = 50.00 SCCM, 25 = 50.00 SCFH
 		6 = 100.0 SCCM, 26 = 100.0 SCFH
 		7 = 200.0 SCCM, 27 = 200.0 SCFH
 		8 = 500.0 SCCM, 28 = 500.0 SCFH
 		9 = 1.000 SLM, 29 = 1.000 SCFM
		10 = 2.000 SLM, 30 = 2.000 SCFM
		11 = 5.000 SLM, 31 = 5.000 SCFM
		12 = 10.00 SLM, 32 = 10.00 SCFM
		13 = 20.00 SLM, 33 = 20.00 SCFM
		14 = 50.00 SLM, 34 = 50.00 SCFM
		15 = 100.0 SLM, 35 = 100.0 SCFM
		16 = 200.0 SLM, 36 = 200.0 SCFM
		17 = 400.0 SLM, 37 = 500.0 SCFM
		18 = 500.0 SLM, 38 = 30.00 SLM
		19 = 1.000 SCMM, 39 = 300.0 SLM


ON c		open valve
 c = 0	 main valve (corresponds to: ON ALL)
 c = 1..4	 channel valve

OF c		close valve 
 c = 0	 main valve (corresponds to: OFF ALL)
 c = 1..4   channel valve 
