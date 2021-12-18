import wpilib, ctre

class Drive:
   def __init__(self, frontLeft, backLeft, frontRight, backRight):
      self.frontLeft = ctre.WPI_TalonSRX(frontLeft)
      self.backLeft = ctre.WPI_TalonSRX(backLeft)

      self.frontRight = ctre.WPI_TalonSRX(frontRight)
      self.backRight = ctre.WPI_TalonSRX(backRight)

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

   def customDrive(self, left_x, left_y, right_x, right_y):
      left_speed = left_y
      right_speed = right_y
      self.setSpeed(left_speed, right_speed)