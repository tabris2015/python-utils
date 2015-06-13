# python-utils
utilidades en python para distintos sensores y módulos, usando raspberry pi  y beaglebone black

### Version
1.0

## MPU6050

MPU6050 es una clase básica para hacer una interfaz con el sensor MEMS acelerómetro + giroscopio MPU6050,
este módulo es muy barato y de fácil adquisición, esta clase lee los valores de los registros del módulo. Está basado en código presentado en este [blog].

### Utilización

```python
#importa el modulo
import MPU6050
#crea un objeto MPU6050
imu = MPU6050()
#lee los valores de aceleracion con get_acc(scaled=True)
(acc_x, acc_y, acc_z) = imu.get_acc()
#lee los valores del giroscopio con get_gyro(scaled=True)
(gyro_x, gyro_y, gyro_z) = imu.get_gyro()

```

### Todo's

La clase es demasiado básica y solo lee los registros por defecto, se necesita:
  - Interfaz completa con el chip
  - Tratamiento básico de los datos

Licencia
----

MIT


**Free Software, Hell Yeah!**

[blog]:http://blog.bitify.co.uk/2013/11/reading-data-from-mpu-6050-on-raspberry.html

