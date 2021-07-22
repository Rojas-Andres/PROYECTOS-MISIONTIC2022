/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.clases;

/**
 *
 * @author ASUS
 */
public class Animal {
    private long id;
    private String name;
    private int agno;

    public Animal() {
    }

    public Animal(long id, String name, int agno) {
        this.id = id;
        this.name = name;
        this.agno = agno;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAgno() {
        return agno;
    }

    public void setAgno(int agno) {
        this.agno = agno;
    }

    @Override
    public String toString() {
        return "Id : "+ this.id + " Nombre : " + this.name + " Años : " + this.agno; //To change body of generated methods, choose Tools | Templates.
    }
    
}
