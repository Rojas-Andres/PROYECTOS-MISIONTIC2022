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
public class Productos {
    private int numeroLote;
    private int fechaCaducidad;
    
    public Productos(){    
    }
    
    public Productos(int numeroLote , int fechaCaducidad){
        this.numeroLote = numeroLote;
        this.fechaCaducidad = fechaCaducidad;
    }  
    
    public int getNumeroLote() {
        return numeroLote;
    }

    public void setNumeroLote(int numeroLote) {
        this.numeroLote = numeroLote;
    }

    public int getFechaCaducidad() {
        return fechaCaducidad;
    }

    public void setFechaCaducidad(int fechaCaducidad) {
        this.fechaCaducidad = fechaCaducidad;
    }
  
}
