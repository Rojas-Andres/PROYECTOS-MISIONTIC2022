import java.util.*;

public class BotonPrueba extends Boton {
    
    //Inserte acá el método constructor
    public BotonPrueba(double ancho,double alto,String colorFondo,String colorTexto,String texto){
        
        super(ancho,alto,colorFondo,colorTexto,texto);
    }
    //Inserte acá la implementación del método abstracto de la clase padre
    @Override
    public void hacerClick(){
        setTexto("Hello World!");
    }
}