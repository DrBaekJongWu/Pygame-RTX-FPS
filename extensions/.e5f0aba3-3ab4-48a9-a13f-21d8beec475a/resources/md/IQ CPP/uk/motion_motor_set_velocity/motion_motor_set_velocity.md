category: motion  
signature: Motor.setVelocity(50, percent);  
device_class: motor  
description: Sets the Motor's velocity.  

# Set Motor Velocity

Встановлює швидкість для мотора VEX IQ.

```cpp
Motor.setVelocity(velocity, units);
```

## Як це працює

`Motor.setVelocity` приймає значення в діапазоні **від -100% до 100%** або **від -127rpm до 127rpm**.

Встановлення швидкості мотора у від'ємне значення змусить його обертатися у зворотному напрямку.

Встановлення швидкості мотора в 0 спричинить його зупинку.

Перша частина команди - назва пристрою.

```cpp
ClawMotor.setVelocity(25, percent);
ArmMotor.setVelocity(75, percent);
```

Встановіть одиниці вимірювання `units` **percent** або **rpm**(revolutions per minute - обертів за хвилину).

## Приклад

Цей приклад встановлює повільне обертання мотора руки зі швидкістю 25% на 90 градусів.

```cpp
ClawMotor.setVelocity(25, percent);
ClawMotor.spinToPosition(90, degrees);
```

<advanced>
</advanced>