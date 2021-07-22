/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mavenproject1;
import java.util.Scanner;

/**
 * Este programa saca el factorial de un numero
 * @author ASUS
 */
public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        long numero = in.nextLong(); // Pedimos el numero
        System.out.println(factorial(numero));
    }
    public static long factorial(long n) {
        long resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }
    
}
