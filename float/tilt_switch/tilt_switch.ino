// Simple testcode for tilt switch
// led lights up when switch it tilted, status printed to serial

int tiltSwitchPin = 9; // connect tilt switch to pin 9
int tiltStatus = 0;
int ledPin = 10; // connect led to pin 10

void setup() {
  pinMode(tiltSwitchPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  tiltStatus = digitalRead(tiltSwitchPin);
  if (tiltStatus == 1) {
    digitalWrite(ledPin, HIGH);
  } else {
    // Otherwise, turn off the LED and print a different message
    digitalWrite(ledPin, LOW);
  }
  Serial.println(tiltStatus); // Print the status to the Serial Monitor
  delay(600); // Delay for stability
  
}
