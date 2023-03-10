int ir_sensor = 2;

int sensor_reading = 0;

void setup(){
  pinMode(ir_sensor,INPUT);
  Serial.begin(9600);
}

void loop(){
  sensor_reading = digitalRead(ir_sensor);
  Serial.println(sensor_reading);
}
