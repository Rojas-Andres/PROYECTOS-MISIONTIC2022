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
import java.util.Arrays;
import java.util.*;
import java.util.Collections;

public class OrdenamientoPersonalizadoE4 {
    public static void main(String[] args){
        
        //int [] vectorEntrada ={0,2,1,65,66,78,12,11,90,13};
        //int [] vectorEntrada ={0,2,1,65};
        int [] vectorEntrada = {13 ,19 ,23 ,709 ,1003 ,5 ,7 ,100};
        int ca = vectorEntrada.length/2;

        Integer [] vector_ini = new Integer[ca];
        Integer [] vector_fin = new Integer[ca];

        //for(int i = 0;i<vector_ini.length;i++){
        //    System.out.println(vector_ini[i]);
        //}

        for(int i = 0;i<vector_ini.length;i++){
            System.out.println(vector_ini[i]);
        }
        for(int i = 0;i<ca;i++){
            vector_ini[i]=vectorEntrada[i];
        }
        System.out.println("");
        for(int i = 0;i<vector_ini.length;i++){
            System.out.println(vector_ini[i]);
        }
        int val = 0  ;
        for(int i = ca;i<vectorEntrada.length;i++){
            vector_fin[val]=vectorEntrada[i];
            val +=1;
        }
        Arrays.sort(vector_ini);
        Arrays.sort(vector_fin, Collections.reverseOrder());
        //Arrays.sort(vector_fin, Collections.reverseOrder());
        for(int i = 0;i<vector_ini.length;i++){
            System.out.println(vector_ini[i]);
        }
        for(int i = 0;i<vector_fin.length;i++){
            System.out.println(vector_ini[i]);
        }
        for(int i = 0;i<vector_ini.length;i++){
            vectorEntrada[i] = vector_ini[i];
        }
        int aux;
        /*
        for(int i = 0; i < vector_fin.length; i++){
            for(int j=i+1; j < vector_fin.length; j++){
                if(vector_fin[i] < vector_fin[j]){
                    aux = vector_fin[i];
                    vector_fin[i] = vector_fin[j];
                    vector_fin[j] = aux;
                }
            }
        }*/
        val = 0;
        for(int i = ca;i<vectorEntrada.length;i++){
            vectorEntrada[i]=vector_fin[val];
            val +=1;
        }


        for(int i = 0;i<vectorEntrada.length;i++){
            System.out.print(vectorEntrada[i]+" ");
        }
    }
}
