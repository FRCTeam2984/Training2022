import wpilib, ctre

class DriveImu:
    def __init__(self, id):
        self.IMU = ctre.PigeonIMU(id)

    def getRotation(self, axis : int):
        # Get the yaw from the IMU
        return self.IMU.getYawPitchRoll()[1][axis]

    def getYaw(self):
        return self.getRotation(0)