package projects.java;

public class Animal 
{

    private String nombre;
    private int edad;
    private String animal;

    public Animal( String nombre, int edad , String animal ) // metodo constructor.
    {
        this.nombre = nombre;
        this.edad = edad;
        this.animal = animal;
    }

    public void animal_info()
    {
        System.out.println("Nombre: " + nombre + "|" + " Edad: " + edad + "|" + " Animal: " + animal + ".");
    }
}
