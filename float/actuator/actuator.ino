// Simple code to test linear actuator
// send 1000 to retract, 2000 to extend

const int actPin = 8;  // The digital pin used for the servo signal

void setup() {
  pinMode(servoPin, OUTPUT);  
}

void loop() {
  // Create a PWM signal manually
  digitalWrite(actPin, HIGH);   // Start the pulse
  delayMicroseconds(2000); // 2000 to extend
  //delayMicroseconds(1000); // 1000 to retract
  digitalWrite(actPin, LOW);    // End the pulse
  delay(20);   // Complete the 20 ms cycle (subtract the pulse width)
  
}
