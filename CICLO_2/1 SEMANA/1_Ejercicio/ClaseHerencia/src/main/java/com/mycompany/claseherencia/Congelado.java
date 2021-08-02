/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.claseherencia;

/**
 *
 * @author ASUS
 */
public class Congelado extends Productos{
    private long temperatura_con;
    private long temperatura_des;
    
    public Congelado(long temperatura_con,long temperatura_des ) {
        this.temperatura_con = temperatura_con;
    }
    
    public Congelado() {
        super();
    }

    public long getTemperatura_con() {
        return temperatura_con;
    }

    public void setTemperatura_con(long temperatura_con) {
        this.temperatura_con = temperatura_con;
    }
    
    public long getTemperatura_des() {
        return temperatura_des;
    }

    public void setTemperatura_des(long temperatura_des) {
        this.temperatura_des = temperatura_des;
    }
    
}
