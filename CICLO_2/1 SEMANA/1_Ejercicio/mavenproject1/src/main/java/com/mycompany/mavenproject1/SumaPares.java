/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mavenproject1;

import static com.mycompany.mavenproject1.Main.factorial;
import java.util.Scanner;

/**
 *
 * @author ASUS
 */
public class SumaPares {
    public static void main(String[] args){
        
        int [] vectorEntrada ={0,2,1,65,66,78,12,11,90,13,-8};
        int suma = 0;
        for(int i = 0; i<vectorEntrada.length;i++ ){
            if (vectorEntrada[i]%2 == 0 && vectorEntrada[i]>0){
                suma += vectorEntrada[i];
            }
        }
        System.out.println(suma);
        
    }
}
