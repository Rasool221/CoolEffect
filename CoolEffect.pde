class balls  
{
  boolean created = false;
 
 public balls() 
 {
   this.generate();
 }
  
  void generate()
  {
    if (this.created == false)
    {
      ellipse(random(0, 400), random(0, 400), 20, 20); 
      this.created = true;
    }
  }
  
}

balls[] arrball;

void setup() 
{
  size(400, 400);
  
  for (int i = 0; i < 10; i++) 
  {
    arrball = (balls[]) append(arrball, new balls());
  }
}


void draw()
{
  
  
}
