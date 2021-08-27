//EL CALIFICADOR GENERARÁ ERROR SI USTED NO IMPLEMENTA TODOS LOS MÉTODOS ESPECIFICADOS EN EL ENUNCIADO
import java.util.ArrayList;
public class Restaurante {

    //Inserte acá los atributos
    public ArrayList<Pedido> pedidos = new ArrayList<Pedido>();

    //Inserte acá el método constructor
    //public Restaurante(ArrayList<Pedido> pedido){
    //    this.pedido = pedido;
    //}
    public Restaurante(){
        
    }
    public ArrayList getPedidos(){
        return pedidos;
    }
    //Inserte acá los SETTERS Y GETTERS

    //Inserte acá los métodos (NO LOS GETTER Y SETTERS)
    public void agregarPedidoLista(Pedido p){
        pedidos.add(p);
    }
    public void eliminarPedido(String pedido){
        for(int i=0;i<pedidos.size();i++){
            if(pedidos.get(i).getnPedido()==pedido){
                pedidos.remove(i);
                break;
            }
            
        }
    }
    public double calcularGanancias(){
        double suma = 0; 
        for(Pedido p: pedidos){
            suma+=p.getCostoPedido();
        }
        return suma;
    }
    public double promedioGananciasTotales(){
        double suma=0;
        double tamano =pedidos.size(); 
        for(Pedido p: pedidos){
            suma+=p.getCostoPedido();
        }
        double promedio = suma / tamano;
        return promedio;
    }
    public double desviacionEstandarGananciasTotales(){
        double suma=0;
        double calculo = 0;
        double total = 0;
        double can = pedidos.size();
        double division = 1 / can;
        for(Pedido p:pedidos){
            calculo = Math.pow(p.getCostoPedido()-promedioGananciasTotales(),2);
            suma+=calculo;
        }
        total = division*suma;
        double finall = Math.sqrt(total);
        return finall;
    }
    public double retornarCostoPedido(String id){
        double costo = 0;
        for(Pedido p:pedidos){
            if(p.getnPedido()==id){
                costo =p.getCostoPedido(); 
                break;
            }
        }
        return costo;
    }
    
}