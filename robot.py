import wpilib
from subsystems import drive, drive_imu
from utils import ID

class MyRobot(wpilib.TimedRobot):

   def robotInit(self):
      self._drive = drive.Drive(ID.DRIVE_LEFT_FRONT, ID.DRIVE_LEFT_BACK, ID.DRIVE_RIGHT_FRONT, ID.DRIVE_RIGHT_BACK)
      self.imu = drive_imu.DriveImu(self._drive.backRight)
      self.left_drivestick = wpilib.Joystick(ID.DRIVE_LEFT_JOYSTICK)
      self.right_drivestick = wpilib.Joystick(ID.DRIVE_RIGHT_JOYSTICK)
      self.back_limit_switch = wpilib.DigitalInput(ID.LIMIT_SWITCH_NC)

   def teleopInit(self):
      pass
      
   def teleopPeriodic(self):
      try:
         self._drive.customDrive(self.left_drivestick.getX(), self.left_drivestick.getY(), self.right_drivestick.getX(), self.right_drivestick.getY())
      except:
         raise
         
      try:
         print(self.imu.getYaw())
      except:
         raise
         

if __name__ == "__main__":
   wpilib.run(MyRobot)