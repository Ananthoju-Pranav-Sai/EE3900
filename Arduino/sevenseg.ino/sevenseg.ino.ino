void sevenseg(int a[])
{
  digitalWrite(2, a[0]); 
  digitalWrite(3, a[1]); 
  digitalWrite(4, a[2]); 
  digitalWrite(5, a[3]); 
  digitalWrite(6, a[4]); 
  digitalWrite(7, a[5]);     
  digitalWrite(8, a[6]); 
}
void setup() 
{
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);            
}
void loop() 
{
 int counts[][7] = {{0,0,0,0,0,0,1},{1,0,0,1,1,1,1},{0,0,1,0,0,1,0},{0,0,0,0,1,1,0}};
 for(int i = 0; i < 4; i++)
 {
  sevenseg(counts[i]);
  delay(1000);
 } 
}
