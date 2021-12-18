import wpilib, ctre

class DriveImu:
    def __init__(self, master):
        self.IMU = ctre.PigeonIMU(master)

    def getRotation(self):
        # Get the yaw from the IMU
        return self.IMU.getYawPitchRoll()[1]

    def getYaw(self):
        return self.getRotation()[0]