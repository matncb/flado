
char msg;
void setup()  
{   
  Serial.begin(9600);

  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);

}  

void nfase(int n)
{
    for (int i = 0; i<n; i++)
    {
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      delay(50);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      delay(50);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
      delay(50);
      digitalWrite(12, LOW);
      digitalWrite(13, LOW);
      delay(50);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      delay(50);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      delay(50);
      digitalWrite(10, HIGH);
      digitalWrite(11, HIGH);
      delay(50);
      digitalWrite(12, HIGH);
      digitalWrite(13, HIGH);
      delay(200);
    }
}

void fase(int n)
{
    for (int i = 0; i<n; i++)
    {
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
      digitalWrite(12, LOW);
      digitalWrite(13, LOW);
      delay(100);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      digitalWrite(10, HIGH);
      digitalWrite(11, HIGH);
      digitalWrite(12, HIGH);
      digitalWrite(13, HIGH);
      delay(100);
    }
}


void loop()  
{ 
  if (Serial.read() == 's')
  {
    nfase(4);
    delay(200);
    Serial.println('l');
  }

}  
    
