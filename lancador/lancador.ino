
int PinoVelocidade = 3; //Ligado ao pino 1 do L293D  
int Entrada1 = 2; //Ligado ao pino 2 do L293D  
int Entrada2 = 7; //Ligado ao pino 7 do L293D 
char msg;
   
void setup()  
{   
  Serial.begin(9600);
  pinMode(PinoVelocidade, OUTPUT);  
  pinMode(Entrada1, OUTPUT);  
  pinMode(Entrada2, OUTPUT);  
}  
//Serial.println("Botao pressionado");]
//c = Serial.read();

void para_motor()  
{  
  digitalWrite(Entrada1, LOW);  
  digitalWrite(Entrada2, LOW);   
} 

void loop()  
{ 
  msg = Serial.read();
  if (msg == 'a')
  {
    int velocidade = 500;  
    analogWrite(PinoVelocidade, velocidade);   
    digitalWrite(Entrada1, LOW);  
    digitalWrite(Entrada2, HIGH);  
    delay(3000);
    para_motor();
    Serial.println("l");
    
  }
 
     
  //para_motor();  
}  
    
