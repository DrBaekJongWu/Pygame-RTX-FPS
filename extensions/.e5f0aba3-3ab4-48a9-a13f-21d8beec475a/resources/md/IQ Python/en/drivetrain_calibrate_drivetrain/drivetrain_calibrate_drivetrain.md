category: drivetrain  
signature: drivetrain.calibrate()  
device_class: drivetrain  
description: Calibrates the Drivetrain's Inertial or Gyro Sensor  

# Drivetrain Calibrate

Calibrates the Drivetrain's Inertial or Gyro Sensor based on which is currently configured with the Drivetrain.

```python
# Inertial Sensor
brain_inertial.calibrate()

# Gyro Sensor
drivetrain_gyro.calibrate()
```

## How To Use

The `Drivetrain Calibrate` command will calibrate the Drivetrain's Inertial or Gyro Sensor. The Drivetrain must remain stationary during the calibration process.

A `wait` should be added after the `Drivetrain Calibrate` command is used to allow for the calibration process to finish correctly.

```python
brain_inertial.calibrate()
wait(3, SECONDS)
```

<advanced>
</advanced>
