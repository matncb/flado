
char msg;
   
void setup()  
{   
  Serial.begin(9600);

  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);

}  

void nfase(int n)
{
    for (int i = 0; i<n; i++)
    {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      delay(75);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
      delay(150);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      delay(75);
      digitalWrite(10, HIGH);
      digitalWrite(11, HIGH);
      delay(150);
    }
}

void fase(int n)
{
    for (int i = 0; i<n; i++)
    {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
      delay(100);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      digitalWrite(10, HIGH);
      digitalWrite(11, HIGH);
      delay(100);
    }
}

void loop()  
{ 
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  msg = Serial.read();
  if (msg == 's')
  {
    nfase(3);
    delay(100);
    Serial.println('l');
    
  } 
}  
    
