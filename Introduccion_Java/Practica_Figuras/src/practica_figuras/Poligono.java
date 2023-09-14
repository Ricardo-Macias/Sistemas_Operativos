
package practica_figuras;

public class Poligono {
    private Double lado;
    private Double numero_lados;
    private Double area;
    private Double angulo;
    private Double apotema;
    
    
    public void setLado(Double lado){
        this.lado = lado;
    }
    
    public Double getLado(){
        return this.lado;
    }
    
    public void setNumero_Lados(Double numero_lados){
        this.numero_lados = numero_lados;
    }
    
    public Double getNumero_Lados(){
        return this.numero_lados;
    }
    
    public void Calcular(){
        this.angulo = Math.toRadians( 360 / (2*this.numero_lados));
        this.apotema = this.lado / (2 * Math.tan(this.angulo));
        this.area = ((this.lado * this.numero_lados) * this.apotema) / 2;
    }
    
    public Double getCalcular(){
        return this.area;
    }
}
