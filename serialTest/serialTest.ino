long randNumber;
byte outputLine;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.setTimeout(1);
}

void loop() {
  if (!Serial.available()){
    
      // print random number
//      randNumber = random(1, 100);
//      Serial.println(randNumber);

      // print incremental bytes
      for (int i = 0; i <= 255; i++) {
      outputLine = byte(i);
      Serial.println(outputLine);
      delay(500);  
      }

  }

  else {
    Serial.println("Serial not available");
  }


  
//  x = Serial.readString().toInt();
//  Serial.print(x + 1);

}
