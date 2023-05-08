const int LED_COUNT = 5;
const int LED_PINS[LED_COUNT] = {2, 3, 4, 5, 6};

void setup() {
  for (int i = 0; i < LED_COUNT; i++) {
    pinMode(LED_PINS[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int val = Serial.read() - '0';
    if (val == 0) {
      for (int i = 0; i < LED_COUNT; i++) {
        digitalWrite(LED_PINS[i], LOW);
      }
    } else if (val >= 1 && val <= LED_COUNT) {
      for (int i = 0; i < LED_COUNT; i++) {
        digitalWrite(LED_PINS[i], i < val);
      }
    }
  }
}
