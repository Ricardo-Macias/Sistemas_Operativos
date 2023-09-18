
package org.Programacion;


public class Celsius {
    private double celsius;
    
    public void setCelsius(double celsius){
        this.celsius = celsius;
    }
    
    public double Celsius_Kelvin(){
        return this.celsius + 273.15;
    }
    
    public double Celsius_Fahrenheit(){
        return (this.celsius * 1.8) + 32;
    }
    
}
