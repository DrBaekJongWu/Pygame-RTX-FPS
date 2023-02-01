category: drivetrain
signature: calibrateDrivetrain(); 
device_class: smartdrive  
description: Calibrates the Smart Drivetrain's Gyro

# kalibroi ajopelin gyro -sensori

kalibroi ajopelin VEX IQ Gyro -sensorin.

```cpp
calibrateDrivetrain();
```

## Miten käytetään

Käytä `calibrateDrivetrain` komentoa ajon alussa kalibroimaan siihen liitetty Gyro -sensori.

```cpp
int main() {
  // kalibroi Gyro -sensori ohjelman alussa
  calibrateDrivetrain();

  // Sitten vasta ajokomennot
  Drivetrain.driveFor(forward, 500, mm);
  Drivetrain.turnToRotation(45, degrees);
}
```

## Esimerkki

Esimerkissä VEX IQ -ajopelin Gyro kalibroidaan ennen 200 mm eteenpäin ajoa ja kääntymistä ajosuuntaan 45 astetta.

```cpp
calibrateDrivetrain();

Drivetrain.driveFor(forward, 200, mm);
Drivetrain.turnToHeading(45, degrees);
```

<advanced>
</advanced>
