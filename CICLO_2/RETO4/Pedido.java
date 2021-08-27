//EL CALIFICADOR GENERARÁ ERROR SI USTED NO IMPLEMENTA TODOS LOS MÉTODOS ESPECIFICADOS EN EL ENUNCIADO
public class Pedido {

    //Inserte acá los atributos
    private String nPedido;
    private String IDCliente;
    private double costoPedido;
    private int diaPedido;
    private int mesPedido;
    private int yearPedido;
    
    public Pedido(String nPedido,String IDCliente,double costoPedido,int diaPedido,int mesPedido,int yearPedido){
        this.nPedido = nPedido;
        this.IDCliente=IDCliente;
        this.costoPedido=costoPedido;
        this.diaPedido=diaPedido;
        this.mesPedido=mesPedido;
        this.yearPedido=yearPedido;
    }
    //Inserte acá el método constructor
    public String getnPedido(){
        return nPedido;
    }
    public String getIDCliente(){
        return IDCliente;
    }
    public double getCostoPedido(){
        return costoPedido;
    }
    public int getDiaPedido(){
        return diaPedido;
    }
    public int getMesPedido(){
        return mesPedido;
    }   
    public int getYearPedido(){
        return yearPedido;
    }
    public void setnPedido(String n){
        this.nPedido = n;
    }
    
    public void setIDCliente(String n){
        this.IDCliente = n;
    }
    public void setCostoPedidoo(double n){
        this.costoPedido = n;
    }
    public void setDiaPedido(int n){
        this.diaPedido = n;
    }
    public void setMesPedido(int n){
        this.mesPedido = n;
    }
    
    public void setYearPedido(int n){
        this.yearPedido = n;
    }
    
    //Inserte acá los SETTERS Y GETTERS
    
    
}