from ctre import WPI_TalonSRX, PigeonIMU
import math

# parameter : type
class Drive:
   #CONTRUCTOR
   def __init__(self, _frontLeft : WPI_TalonSRX, _backLeft : WPI_TalonSRX, _frontRight : WPI_TalonSRX, _backRight : WPI_TalonSRX, _drive_imu : PigeonIMU):
      self.frontLeft = _frontLeft
      self.backLeft = _backLeft

      self.frontRight = _frontRight
      self.backRight = _backRight
      
      self.drive_imu = _drive_imu

   #HELPER FUNCTIONS
   def setRightSpeed(self, speed):
      # speed is a float value from -1 to 1
      speed = max(-1, min(speed, 1))
      self.frontRight.set(speed)
      self.backRight.set(speed)

   def setLeftSpeed(self, speed):
      # speed is a float value from -1 to 1
      speed = max(-1, min(speed, 1))
      self.frontLeft.set(speed)
      self.backLeft.set(speed)
   
   def setSpeed(self, left, right):
      self.setLeftSpeed(left)
      self.setRightSpeed(right)

   def getRotation(self):
        # Get the yaw from the IMU
        return self.drive_imu.getYawPitchRoll()[1]

   def getYaw(self):
        return self.getRotation()[0]

   #DRIVE FUNCTIONS
   def arcadeDrive(self, y, x):
      left_speed = y + x
      right_speed = y - x
      self.setSpeed(left_speed, right_speed)

   def centralDrive(self, speed, y, x):
      # speed is a float value from -1 to 1
      cur_rotation = self.getYaw()
      # Using atan2, it assures that only the shortest way will be used to get to the desired angle and not the 
      # long route possibly recieved by using just the math.atan function.
      end_rotation = math.atan2(y, x)
      # Use PID or something in this next step idk
      left_speed = speed
      right_speed = speed
      self.setSpeed(left_speed, right_speed)
      # this function is NOT finished. It should be based on a two axis joystick determing rotation and one 
      # joystick controlling the speed. The motors should rotate to the angle a two axis joystick points