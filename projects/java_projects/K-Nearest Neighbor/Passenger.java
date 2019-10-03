import java.util.*;

public class Passenger{
	
private String name;
private double fare;
private int pClass;
private int gender;
private String fate;
   
public Passenger(String[] arr){
	

	for(int i = 0; i < arr.length; i++){
		if(arr[i].matches("[A-Z]{1}[a-z]+[A-Z]{1}[a-z]+"))
		{
         String str1 = arr[i].replaceAll("(?!^)([A-Z])", " $1");
      
         String[] strSplit = str1.split(" ");
      
         String lastName = strSplit[0];
         String firstName = strSplit[1];
         String fullName = firstName + " " + lastName;
      
			this.name = fullName;	 
	    }
		else if(arr[i].matches("[0-9]+\\.[0-9]{1}"))
		{
			double fare = Double.parseDouble(arr[i]);
			this.fare = fare;
	    }
		else if(arr[i].contains("First"))
		{
			this.pClass = 1;
		}
		else if(arr[i].contains("Second"))
		{
			this.pClass = 2;
	    }
		else if(arr[i].contains("Third"))
	    {
			this.pClass = 3;
	    }
		else if(arr[i].contains("Male"))
	    {
			this.gender = 0;
	    }
		else if(arr[i].contains("Female"))
	    {
			this.gender = 1;
	    }
		else if(arr[i].contains("live")){
			this.fate = "live";
		}
		else if(arr[i].contains("die")){
			this.fate = "dead";
		}
	}
}
 
public void setFate(String fate){
	this.fate = fate;
}
     
public String getName()
{
    return this.name;
}
     
public double getFare()
{
    return this.fare;
}
     
public int getPClass()
{
    return this.pClass;
}
     
public int getGender()
{
    return this.gender;
}

public String getFate(){
	return this.fate;
}
}