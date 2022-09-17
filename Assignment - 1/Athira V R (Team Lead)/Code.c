int led = 8;
int trig = 2;
int echo = 5;
int buzzer = 4;
  
void setup()
{
  Serial.begin(9000);
  pinMode(led,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(buzzer,OUTPUT);
}

void loop()
{
  double a = analogRead(A2);
  double v = a / 1024;
  double tvolt = v * 5;
  double o = tvolt - 0.5;
  double t = 0 * 100;
  Serial.print("Temperature in degree");
  Serial.println(t);
  if(t >= 50)
  {
    digitalWrite(led,HIGH);
  }
  else
  {
    digitalWrite(led,LOW);
  }
  digitalWrite(trig,LOW);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  float dur = pulseIn(echo,HIGH);
  float dist = (dur * 0.343)/2;
  Serial.print("Distance");
  Serial.println(dist);
  if(dist >= 17)
  {
    digitalWrite(buzzer,HIGH);
  }
  else
  {
    digitalWrite(buzzer,LOW);
  }
}
