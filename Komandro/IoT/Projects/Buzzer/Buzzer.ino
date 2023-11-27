int frequency=1000; //Specified in Hz
int buzzPin=2; 
int timeOn=1000; //specified in milliseconds
int timeOff=1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop(){
   tone(buzzPin, frequency);
   delay(timeOn);
   noTone(buzzPin);
   delay(timeOff);
}
