int led1=13;
int led2=12;
int led3=8;
int led4=7;
int led5=4;
int led6=2;
int valor=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  pinMode(led5,OUTPUT);
  pinMode(led6,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
  {
    char opcion =Serial.read();

    if(opcion=='a')
    {
      digitalWrite(led1,HIGH);
    }
    if(opcion=='b')
    {
      digitalWrite(led1,LOW);
    }
    if(opcion=='c')
    {
      digitalWrite(led2,HIGH);
    }
    if(opcion=='d')
    {
      digitalWrite(led2,LOW);
    }
    if(opcion=='e')
    {
      digitalWrite(led3,HIGH);
    }
    if(opcion=='f')
    {
      digitalWrite(led3,LOW);
    }
    if(opcion=='g')
    {
      digitalWrite(led4,HIGH);
    }
    if(opcion=='h')
    {
      digitalWrite(led4,LOW);
    }
    if(opcion=='i')
    {
      digitalWrite(led5,HIGH);
    }
    if(opcion=='j')
    {
      digitalWrite(led5,LOW);
    }
    if(opcion=='k')
    {
      digitalWrite(led6,HIGH);
    }
    if(opcion=='l')
    {
      digitalWrite(led6,LOW);
    }
  }
  else
  {
    if(analogRead(0)>0)
    {
    valor=analogRead(0);
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,HIGH);
    digitalWrite(led5,HIGH);
    digitalWrite(led6,HIGH);}
    else if(analogRead(1)>0 )
    {
    valor=analogRead(1);
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,HIGH);
    digitalWrite(led5,HIGH);
    digitalWrite(led6,HIGH);}
    else if(analogRead(2)>0)
    {
    valor=analogRead(2);
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,HIGH);
    digitalWrite(led5,HIGH);
    digitalWrite(led6,HIGH);}
    else if(analogRead(3)>0)
    {
    valor=analogRead(3);
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,HIGH);
    digitalWrite(led5,HIGH);
    digitalWrite(led6,HIGH);}
    else{
    valor=analogRead(0);
    /*digitalWrite(led1,LOW);
    digitalWrite(led2,LOW);
    digitalWrite(led3,LOW);
    digitalWrite(led4,LOW);
    digitalWrite(led5,LOW);
    digitalWrite(led6,LOW);*/}
    Serial.println(valor);
    delay(100);
  }
}
