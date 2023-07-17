int sensoroutput = 3; // the analog pin connected to the sensor
int ledoutput = 0; // pin connected to LED
int THRESHOLD = 100;

void setup()
{
pinMode(LED_BUILTIN, OUTPUT);   // this function is used to declare led connected pin as output
}
void loop()
{
int value = analogRead(sensoroutput);  // function to read analog voltage from sensor
Serial.println(value);
if(value>0){
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
}
}