category: drivetrain  
signature: turn_gyro_smart.calibrate()
device_class: drivetrain  
description: Calibrates the Drivetrain.  

# Ajopelin gyron kalibrointi

Kalibroi ajopelin gyro.

```python
turn_gyro_smart.calibrate()
```

## Miten käytetään

`turn_gyro_smart.calibrate()` komento kalibroi ajopelin gyron. Ajopelin pitää olla paikallaan kalibroinnin ajan.

Komento `wait` potää lisätä ennen komentoa `turn_gyro_smart.calibrate()`, jotta kalibrointi onnistuu.

```python
turn_gyro_smart.calibrate()
wait(3, SECONDS)
```

<advanced>
</advanced>
