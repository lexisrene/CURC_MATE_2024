// Simple test code for Real Time Clock module
// Set date using rtc.setTime(<hour>, <minute>, <second>)

#include <DS3231.h>

DS3231  rtc(SDA, SCL);

void setup()
{
  // Setup Serial connection
  Serial.begin(115200);
  // Uncomment the next line if you are using an Arduino Leonardo
  //while (!Serial) {}
  
  // Initialize the rtc object
  rtc.begin();
  
  // The following lines can be uncommented to set the date and time
  //rtc.setTime(05, 27, 0);     // Set the time to 12:00:00 (24hr format)
}
void loop()
{
  // Send time
  Serial.println(rtc.getTimeStr());
  
  // Wait one second before repeating
  delay (1000);
}
