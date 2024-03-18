package Java.proyecto01;

import java.util.Scanner;

public class proyecto01 
{
    public static void main ( String[] args ) 
    {
        Scanner input = new Scanner(System.in); // pedir información


        String nombre; // almacenar (guardar) nombre.

        System.out.print("Entre su nombre: "); // mostrar mensaje
        nombre = input.nextLine(); // usamos el input para guardar el nombre en la variable nombre.

        System.out.printf("El nombre es: %s", nombre); // saludamos al usuario.

        input.close();
    }
}