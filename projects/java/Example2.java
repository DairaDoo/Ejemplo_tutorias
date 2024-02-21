package projects.java;

import java.util.Scanner; // importamos 

public class Example2 
{
    public static void main ( String[] args )
    {

        Scanner input = new Scanner( System.in ); // creamos la instancia de la clase Scanner.

        String nombre; // Variable para almacenar nombre.

        System.out.print("Entre su nombre: ");
        nombre = input.nextLine();

        System.out.println( "El nombre de la persona es: " + nombre );


        input.close();

    }    
}
