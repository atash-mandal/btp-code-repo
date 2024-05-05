import skmd as md
import numpy as np
import math

class Stub:
	# <--- l1 ---->             <---- l2 ---->
	# o--------------------------------------o ^
	# 		Z0, \gamma = \alpha + j\beta       w
	# o------------o-----------o-------------o v
	#			   |           |  ^
	#			   |     Z0    |  |
	#			   |           |  |
	#			   |           |  l0
	#			   |  is_open  |  |
	#			   |           |  |
	#			   o<---w0 --->o  v

	def __init__(self, l0, w0, l1, l2, w, h, er, is_open=True,omega=None, text_tag='Stub'):
		self.l0 = l0
		self.w0 = w0
		self.l1 = l1
		self.l2 = l2
		self.w = w
		self.h = h
		self.er = er
		self.omega = omega
		self.is_open = is_open
		self.text_tag = text_tag
		strip_line_1 = md.structure.Microstripline(er=er,h=h,l=l1,w=w,omega=omega)
		strip_line_2 = md.structure.Microstripline(er=er,h=h,l=l2,w=w,omega=omega)

		self.get_Z0()
		self.c = 299792458.0
		self.vp = self.c/np.sqrt(self.er_eff)
		self.beta = self.omega/self.vp
		self.gamma = 1j*self.beta

		beta = 2 * np.pi * self.omega * np.sqrt(self.er_eff) / self.c
		theta = beta * self.l0

		if is_open:
			A = np.ones(len(self.omega))
			B = np.zeros(len(self.omega))
			C = (1 / self.Z0) * 1j * np.tan(theta)
			D = np.ones(len(self.omega))
		else:
			A = np.cosh(1j * self.beta * self.l1)
			B = 1j * self.Z0 * np.sinh(1j * self.beta * self.l1)
			C = 1j * self.Z0 * np.sinh(1j * self.beta * self.l1)
			D = np.cosh(1j * self.beta * self.l1)

		stub_net = md.network.Network(A, B, C, D, parameter='abcd',Z0=self.Z0,omega=self.omega)	
		self.NW = strip_line_1.NW * stub_net * strip_line_2.NW
            
	def get_Z0(self):
		""" Computes Z0 and er_eff for given microstrip line parameters
		Ref: Page-49, Section-4.1.4
		"""
		c = 299792458  # Speed of light (m/s)
		u = self.w0/self.h
		a = 1 + 1/49 * np.log((u**4 + (u/52)**2 ) /(u**4 + 0.432 ) ) \
			+ 1/18.7 * np.log(1+(u/18.1)**3 )
		b = 0.564*((self.er-0.9)/(self.er +3) )**0.053
		self.er_eff = (self.er + 1)/2 + 0.5*(self.er - 1)*(1 + 10/u)**(-a*b) # Eq 4.4
		F = 6 + (2*np.pi -6)*np.exp(-(30.666/u)**0.7528)
		self.Z0 = 120*np.pi/(2*np.pi*np.sqrt(self.er_eff)) * np.log(F/u + np.sqrt(1+(2/u)**2)) # Eq 4.5


		


