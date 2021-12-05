import wpilib, ctre

class Drive:
   def __init__(self):
      self.frontLeft = ctre.WPI_TalonSRX(3)
      self.backLeft = ctre.WPI_TalonSRX(4)
      self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.backLeft)

      self.frontRight = ctre.WPI_TalonSRX(1)
      self.backRight = ctre.WPI_TalonSRX(2)
      self.right = wpilib.SpeedControllerGroup(self.frontRight, self.backRight)

   def setRightSpeed(self, speed):
      # speed is a float value from -1 to 1
      speed = max(-1, min(speed, 1))
      self.right.set(speed)

   def setLeftSpeed(self, speed):
      # speed is a float value from -1 to 1
      speed = max(-1, min(speed, 1))
      self.left.set(speed)
   
   def customDrive(self, left_x, left_y, right_x, right_y):
      left_speed = left_y + left_x / 5
      right_speed = left_y - left_x / 5
      self.setRightSpeed(right_speed)
      self.setLeftSpeed(left_speed)