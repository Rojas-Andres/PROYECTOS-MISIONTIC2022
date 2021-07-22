/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mavenproject1;

/**
 *
 * @author ASUS
 */
public class Media {
    public static void main(String[] args){
        
        int [] vectorEntrada ={0,2,1,65,66,78,12,11,90,13,-8};
        float suma = 0;
        for(int i = 0; i<vectorEntrada.length;i++ ){
            if (vectorEntrada[i]%2 == 0 && vectorEntrada[i]>0){
                suma += vectorEntrada[i];
            }
        }
        float promedio = suma / vectorEntrada.length;
        System.out.println(promedio);
        
    }
}
