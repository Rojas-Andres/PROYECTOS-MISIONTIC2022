public class CuentaAhorro extends CuentaBanco {

    //Inserte acá el método constructor
    public CuentaAhorro(String numeroCuenta,String nombrePropietario,double saldo){
        super(numeroCuenta,nombrePropietario,saldo);
    }
    //Inserte acá los métodos (NO LOS GETTER Y SETTERS)
    public double getIEA(){
        double re = 0;
        if(getSaldo()<1000000){
            re = getSaldo() * (1 + ( 0.01 / 365) );
        }
        else if(getSaldo()>=1000000 && getSaldo()<2000000){
            re = getSaldo() * (1 + (0.0175/365) );
        }
        else if(getSaldo() >=2000000){
            re = getSaldo() * ( 1+ (2.3/365));
        }
        return re;
    }
    public void pagarInteres(int dias){
        double c =0.1;
        
        setSaldo(10);
    }
}