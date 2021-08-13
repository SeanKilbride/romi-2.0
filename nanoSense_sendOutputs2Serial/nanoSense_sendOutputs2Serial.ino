int d0 = 0;
int d1 = 0;
int d2 = 0;
int d3 = 0;
int d4 = 0;
int d5 = 0;
int d6 = 0;
int d7 = 0;


void setup() {
  // put your setup code here, to run once:

  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  
  // set the digital pins as inputs:
  pinMode(LED_BUILTIN, OUTPUT);
  
  for (int i = 0; i <= 7; i++) {
//    Serial.print("Setting pinMode for ");
//    Serial.print(i);
//    Serial.println();
    pinMode(i, INPUT);
//    delay(500);
  }
  
//  pinMode(0,     INPUT);
//  pinMode(1,     INPUT);
//  pinMode(2,     INPUT);
//  pinMode(3,     INPUT);
//  pinMode(4,     INPUT);
//  pinMode(5,     INPUT);
//  pinMode(6,     INPUT);
//  pinMode(7,     INPUT);


}

void loop() {
  // put your main code here, to run repeatedly:


  d0 = digitalRead(0);
  Serial.println(d0);
  Serial.print(" ");

  d1 = digitalRead(1);
  Serial.println(d1);
  Serial.print(" ");

  d2 = digitalRead(2);
  Serial.println(d2);
  Serial.print(" ");

  d3 = digitalRead(3);
  Serial.println(d3);
  Serial.print(" ");

  d4 = digitalRead(4);
  Serial.println(d4);
  Serial.print(" ");

  d5 = digitalRead(5);
  Serial.println(d5);
  Serial.print(" ");

  d6 = digitalRead(6);
  Serial.println(d6);
  Serial.print(" ");

  d7 = digitalRead(7);
  Serial.println(d7);
  Serial.print(" ");
 
  delay(300);
  

}
