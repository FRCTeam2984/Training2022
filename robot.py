import wpilib
from subsystems import drive

class MyRobot(wpilib.TimedRobot):

   def robotInit(self):
      self.drive = drive.Drive()
      self.left_drivestick = wpilib.Joystick(0)
      self.right_drivestick = wpilib.Joystick(1)
   
   def teleopInit(self):
      pass

   def teleopPeriodic(self):
      self.drive.customDrive(self.left_drivestick.getX(), self.left_drivestick.getY(), self.right_drivestick.getX(), self.right_drivestick.getY())

if __name__ == "__main__":
   wpilib.run(MyRobot)