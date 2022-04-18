
char msg;
   
void setup()  
{   
  Serial.begin(9600);

  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

}  

void loop()  
{ 
  msg = Serial.read();
  if (msg == 's')
  {
    for (int i = 0; i<5; i++)
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
    delay(100);
    Serial.println('l');
    
  }
 
     
  //para_motor();  
}  
    
