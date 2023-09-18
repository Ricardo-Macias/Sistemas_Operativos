
package org.Programacion;

public class Fahrenheit {
    
    private double valor;
    
    public void setValor(double valor){
        this.valor = valor;
    }
    
    public double Fahrenheit_Celsius(){
        return (this.valor - 32)/1.8;
    }
    
    public double Fahrenheit_Kelvin(){
        return (this.valor + 459.67) * 5 / 9;
    }
    
}
