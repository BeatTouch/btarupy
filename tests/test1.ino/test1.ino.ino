// the analog pin connected to the piezo plates
int piezoInput1 = 1;
int piezoInput2 = 4;

// pin connected to LED
int ledoutput1 = 8;
int ledoutput2 = 11;

int THRESHOLD = 100;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(ledoutput1, OUTPUT);
  pinMode(ledoutput2, OUTPUT);
}

void loop()
{
  int ppovalue = analogRead(piezoInput1);
  int pptvalue = analogRead(piezoInput2);

  if(ppovalue>0){
    digitalWrite(ledoutput1, HIGH);
    delay(100);
    digitalWrite(ledoutput1, LOW);
  }

  if(pptvalue>0){
    digitalWrite(ledoutput2, HIGH);
    delay(100);
    digitalWrite(ledoutput2, LOW);
  }
}
