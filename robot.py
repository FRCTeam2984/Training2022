import wpilib, ctre
from utils import ID
from subsystems import drive
from commands import turn_to_angle
from networktables import NetworkTables

NetworkTables.initialize(server='10.29.84.2')
sd = NetworkTables.getTable("SmartDashboard")
class MyRobot(wpilib.TimedRobot):

   def robotInit(self):
      #components: These are classes representing all the electrical sensors and actuators on the robot.
      self.frontLeft = ctre.WPI_TalonSRX(ID.DRIVE_LEFT_FRONT)
      self.backLeft = ctre.WPI_TalonSRX(ID.DRIVE_LEFT_BACK)

      self.frontRight = ctre.WPI_TalonSRX(ID.DRIVE_RIGHT_FRONT)
      self.backRight = ctre.WPI_TalonSRX(ID.DRIVE_RIGHT_BACK)

      self.drive_imu = ctre.PigeonIMU(self.backRight)
      self.back_limit_switch = wpilib.DigitalInput(ID.LIMIT_SWITCH_NC)

      # Might change to XBOX controller depending on it working or not.
      self.drive_stick = wpilib.XboxController(ID.DRIVE_JOYSTICK)
      self.operator_stick = wpilib.XboxController(ID.OPERATOR_JOYSTICK)
      self.x_axis = self.operator_stick.Axis(0)
      #subsystems: These combine multiple components into a coordinated system.
      self._drive = drive.Drive(self.frontLeft, self.backLeft, self.frontRight, self.backRight, self.drive_imu)
      
      #commands: These utilize subsystems to perform autonomous routines.

   def teleopInit(self):
      self.frontLeft.setInverted(False)
      self.backLeft.setInverted(False)
      self.frontRight.setInverted(False)
      self.backRight.setInverted(False)
      
   def teleopPeriodic(self):
      sd.putNumber("Drive Joystick LX", self.x_axis)

      sd.putBoolean("A Button", self.drive_stick.getAButtonPressed())
      # Exceptions are used to not crash robot code if in competition, 
      # but in our testing case we are raising the exceptions because we want to debug.
      try:
         if self.drive_stick.getAButtonPressed() == True:
            self._drive.arcadeDrive(self.drive_stick.getY(), self.drive_stick.getX())
         else:
            self._drive.centralDrive(self.drive_stick.getZ(), self.drive_stick.getY(), self.drive_stick.getX())
      except:
         pass
         
         

if __name__ == "__main__":
   wpilib.run(MyRobot)