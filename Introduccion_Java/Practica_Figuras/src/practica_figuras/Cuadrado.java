
package practica_figuras;


public class Cuadrado {
    private Double lado;
    private Double area;
    
    public void setLado(Double lado){
        this.lado = lado;
    }
    
    public Double getLado(){
        return this.lado;
    }
    
    public void Calcular(){
        this.area = this.lado * this.lado;
    }
    
    public Double getCalcular(){
        return this.area;
    }
    
}
