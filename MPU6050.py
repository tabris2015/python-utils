import smbus
import math

class MPU6050(object):
	"""clase para el acelerometro MPU6050"""
	# direccion del dispositivo
	address = 0x68
	# registros del dispositivo
	power_mgmt_1 = 0x6b
	power_mgmt_2 = 0x6c
	ADD_GYRO_X = 0X43
	ADD_GYRO_Y = 0X45
	ADD_GYRO_Z = 0X47
	ADD_ACC_X = 0X3B
	ADD_ACC_Y = 0X3D
	ADD_ACC_Z = 0X3F

	# atributos del objeto
	GYRO_X = 0
	GYRO_Y = 0
	GYRO_Z = 0
	ACC_X = 0
	ACC_Y = 0
	ACC_Z = 0


	bus = smbus.SMBus(1)
	# -- metodos para el i2c -- #
	def read_byte(self,adr):
	    return self.bus.read_byte_data(self.address, adr)

	def read_word(self, adr):
	    high = self.bus.read_byte_data(self.address, adr)
	    low = self.bus.read_byte_data(self.address, adr+1)
	    val = (high << 8) + low
	    return val

	def read_word_2c(self, adr):
	    val = self.read_word(adr)
	    if (val >= 0x8000):
	        return -((65535 - val) + 1)
	    else:
	        return val

	def dist(self,a,b):
	    return math.sqrt((a*a)+(b*b))

	def get_y_rotation(self,x,y,z):
	    radians = math.atan2(x, dist(y,z))
	    return -math.degrees(radians)

	def get_x_rotation(self,x,y,z):
	    radians = math.atan2(y, dist(x,z))
	    return math.degrees(radians)
	
	def get_gyro(self, scaled = True):
		x = self.read_word_2c(self.ADD_GYRO_X)
		y = self.read_word_2c(self.ADD_GYRO_Y)
		z = self.read_word_2c(self.ADD_GYRO_Z)
		if scaled:
			return (x / 131.0, y / 131.0, z / 131.0)
		else:
			return (x, y, z)

	def get_acc(self, scaled = True):
		x = self.read_word_2c(self.ADD_ACC_X)
		y = self.read_word_2c(self.ADD_ACC_Y)
		z = self.read_word_2c(self.ADD_ACC_Z)
		if scaled:
			return (x / 16384.0, y / 16384.0, z / 16384.0)
		else:
			return (x, y, z)
