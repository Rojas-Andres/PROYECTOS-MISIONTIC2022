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
public class Clases {
    public static void main(String[] args){
        //Creamos con los atributos vacios
        Animal an = new Animal();
        System.out.println(an.toString());
        Animal an2 = new Animal(1,"Perro",5);
        System.out.println(an2.toString());
        // Cambiamos la edad del animal
        an2.setAgno(20);
        System.out.println(an2.toString());
    }
}
