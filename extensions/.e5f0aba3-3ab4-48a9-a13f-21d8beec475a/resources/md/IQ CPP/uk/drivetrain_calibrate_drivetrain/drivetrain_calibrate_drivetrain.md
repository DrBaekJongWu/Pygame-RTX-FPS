category: drivetrain
signature: calibrateDrivetrain(); 
device_class: smartdrive  
description: Calibrates the Smart Drivetrain's Gyro

# Calibrate Drivetrain

Калібрує трансмісію, якщо налаштовано гіроскопічний датчик VEX IQ.

```cpp
calibrateDrivetrain();
```

## Як це працює

Виклик команди `calibrateDrivetrain` на початку програми для калібрування трансмісії.

```cpp
int main() {
  // Калібрування трансмісії на початку головної функції
  calibrateDrivetrain();

  // Сюди додавати інший код
  Drivetrain.driveFor(forward, 500, mm);
  Drivetrain.turnToRotation(45, degrees);
}
```

## Приклад

Цей приклад калібрує трансмісію VEX IQ перед рухом вперед на 200 мм і поворотом на курс 45 градусів.

```cpp
calibrateDrivetrain();

Drivetrain.driveFor(forward, 200, mm);
Drivetrain.turnToHeading(45, degrees);
```

<advanced>
</advanced>
