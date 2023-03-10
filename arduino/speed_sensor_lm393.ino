//#include "TimerOne.h"
//
//int speed_sensor = 2;
//int motor = 3;
//int counter=0;
//
//void countMotorRotation(){
//  counter++;
//}
//
//void timerIsr(){
//  Timer1.detachInterrupt();
//  Serial.println("Motor Speed: ");
//  int rotation = counter / 20;
//  Serial.println(rotation);
//  counter = 0; // reset counter
//  Timer1.attachInterrupt(timerIsr);
//}
//
//
//void setup() {
//  pinMode(speed_sensor,INPUT);
//  pinMode(motor,OUTPUT);
//  Serial.begin(9600);
//
//  Timer1.initialize(1000000);
//  attachInterrupt(0,countMotorRotation,RISING);
//  Timer1.attachInterrupt(timerIsr);
//}
//
//void loop() {
//  //  = digitalRead(speed_sensor);
//  // Serial.println(sensor_reading);
//
//}
