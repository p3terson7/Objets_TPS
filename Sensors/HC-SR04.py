from hcsr04sensor import sensor

trigger_pin = 23
echo_pin = 25
value = sensor.Measurement(trigger_pin, echo_pin)

raw_measurement = value.raw_distance()

distance_cm = value.distance_metric(raw_measurement)

print(f"Distance: {distance_cm} cm")
