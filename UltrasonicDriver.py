from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor
from CameraPanDriver import AngularSweep 
from time import sleep
import os


class UltraSonicControl(AngularSweep):
	ECHO_PIN = 23
	TRIGGER_PIN = 24
	Threshold_Distance = 40
	SensorObject  = ""
	
	def __init__(self):
		super().__init__()
		factory = PiGPIOFactory()
		print("factory init for Ultrasonic")
		self.SensorObject =DistanceSensor(echo=self.ECHO_PIN,trigger=self.TRIGGER_PIN,pin_factory=factory)#,max_distance=1000,threshold_distance=Threshold_Distance)
		while True:
			print(f"Connecting To Ultrasonic ..{self.SensorObject.distance}")
			if self.SensorObject.distance>=0:
				break
			sleep(0.5)
				
		print("UltrasonicSensor Connnection Successfull")
	
	def clearAhead(self,get_distance = False):
		AlertDistance = self.Threshold_Distance/100
		if self.SensorObject.distance <= AlertDistance:
			if get_distance:
				return True,self.SensorObject.distance
			else:
				return True
		else:
			return False
	
	def UltrasonicLookLeft(self,angle_left = 90):
		self.HorizontalAngleChange(angle_left)
	def UltrasonicLookRight(self,angle_right = 90):
		self.VerticalAngleChange(angle_right)
	
	def UltraSonicFreeSweep(self):
		self.FreeSweep("horizontal")
	def UltrasonicLookInFront(self):
		self.AutoReset(1098)
	

		
		
if  __name__ =="__main__":
	UltraSonicControl().UltrasonicLookInFront()
	UltraSonicControl().UltraSonicFreeSweep()
