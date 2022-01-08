import wpilib

#Unused class
class DriveImu:
    def __init__(self, _imu):
        self.imu = _imu

    def getRotation(self):
        # Get the yaw from the IMU
        return self.imu.getYawPitchRoll()[1]

    def getYaw(self):
        return self.getRotation()[0]