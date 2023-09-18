
package org.Programacion;


public class Kelvin {
    
    private double valor;
    
    public void setValor(double valor){
        this.valor = valor;
    }
    
    public double Kelvin_Celsius(){
        return this.valor - 273.15;
    }
    
    public double Kelvin_Fahrenheit(){
        return ((this.valor - 273.15)*1.8) + 32;
    }
        
    
}
