#include<iostream>
using namespace std;
int addition(int a,int b)
{
    return(a+b);
}
int subtraction(int a,int b)
{
    return(a-b);
}
int multiplication(int a,int b)
{
    return(a*b);
}
int division(int a,int b)
{
    return(a/b);
}
int moddivision(int a,int b)
{
    return(a%b);
}
int main()
{
  int a,b;
  char c;
  cout<<"Input Two numbers ";
  cin>>a>>b;
  cout<<"\nPress + for Addition ";
  cout<<"\nPress - for Subtraction ";
  cout<<"\nPress * for Multiplication ";
  cout<<"\nPress / for Division ";
  cout<<"\nPress % for Mod Division ";
  cout<<"\nInput Your Choice ";
  cin>>c;
  switch (c)
  {
  case '+':
    cout<<"\nAddition = "<<addition(a,b);
    break;
    case '-':
    cout<<"\nSubtraction = "<<subtraction(a,b);
    break;
    case '*':
    cout<<"\nMultiplication = "<<multiplication(a,b);
    break;
    case '/':
    cout<<"\nDivision = "<<division(a,b);
    break;
    case '%':
    cout<<"\nMod Division = "<<moddivision(a,b);
    break;
    default :
        cout<<"\nInvalid choice";
  }
  return 0;

}
