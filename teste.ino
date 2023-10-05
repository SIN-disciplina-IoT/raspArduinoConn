int led = 12;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == "l"){
      digitalWrite(led, HIGH);
    }
    else{
      digitalWrite(led, LOW);
    }
  }
}
