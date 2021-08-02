import java.util.*;

public class Personaje{
    //Inserte acá los atributos
    private String nombre;
    private double posicionX = 0;
    private double posicionY = 0;
    private char sexo;
    private double distanciaTotal = 0;
    private int numeroBotiquines = 0;
    private double vida = 100;

    //Inserte acá el método constructor
    public Personaje(String nombre,char sexo){
        this.nombre = nombre;
        this.sexo = sexo;
    }
    
    
    //Inserte acá los métodos (NO LOS GETTER Y SETTERS)
    
    public void usarBotiquin(){
        if(this.numeroBotiquines != 0 ){
            this.numeroBotiquines -=1; 
            this.vida +=5;
        }
    }
    
    public void recogerBotiquin(){
        this.numeroBotiquines +=1;
    }
    
    public void moverDerecha(int d){
        this.posicionX +=d;
        this.distanciaTotal +=d; 
    }
    
    public void moverIzquierda(int d){
        this.posicionX -=d;
        this.distanciaTotal +=d;
        
    }
    public void moverArriba(int d){
        this.posicionY +=d;
        this.distanciaTotal +=d;
    }
    public void moverAbajo(int d){
        this.posicionY -=d;
        this.distanciaTotal +=d;
    }
    public double calcularDistanciaRespectoOrigen(){
        return Math.sqrt(Math.pow(posicionX,2) + Math.pow(posicionY,2));
    }
    
    //Inserte acá los SETTERS Y GETTERS
    public double getPosicionX() {
        return posicionX;
    }
    
    public void setPosicionX(double posicionX) {
        this.posicionX = posicionX;
    }

    public double getPosicionY() {
        return posicionY;
    }

    public void setPosicionY(double posicionY) {
        this.posicionY = posicionY;
    }

    public char getSexo() {
        return sexo;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }

    public double getDistanciaTotal() {
        return distanciaTotal;
    }

    public void setDistanciaTotal(double distanciaTotal) {
        this.distanciaTotal = distanciaTotal;
    }

    public int getNumeroBotiquines() {
        return numeroBotiquines;
    }

    public void setNumeroBotiquines(int numeroBotiquines) {
        this.numeroBotiquines = numeroBotiquines;
    }

    public double getVida() {
        return vida;
    }

    public void setVida(double vida) {
        this.vida = vida;
    }
    public String getNombre(){
        return nombre;
    }
    
}