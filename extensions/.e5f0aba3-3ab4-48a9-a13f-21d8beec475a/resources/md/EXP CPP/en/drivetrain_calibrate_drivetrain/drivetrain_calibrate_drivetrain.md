category: drivetrain  
signature: calibrateDrivetrain();  
device_class: drivetrain  
description: Calibrates the Drivetrain.  

# Drivetrain Calibrate

Calibrates the Drivetrain.

```cpp
calibrateDrivetrain();
```

## How To Use

Call the `calibrateDrivetrain` command at the start of the program to calibrate the Drivetrain.

```cpp
int main() {
  // Calibrate the Drivetrain at the top of the main function
  calibrateDrivetrain();

  // Add other program code here
  Drivetrain.driveFor(forward, 500, mm);
  Drivetrain.turnToRotation(45, degrees);
}
```
## Example

This example will calibrate the VEX EXP Drivetrain before driving 200 mm forward and turning to heading 45 degrees.

```cpp
calibrateDrivetrain();

Drivetrain.driveFor(forward, 200, mm);
Drivetrain.turnToHeading(45, degrees);
```

<advanced>
</advanced>

