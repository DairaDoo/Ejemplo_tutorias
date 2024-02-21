package projects.java;

import java.util.HashMap;
import java.util.Map;

public class Nada 
{
    public static void main ( String[] args )
    {
        HashMap < String, Integer > listaDeJugadores = new HashMap < String, Integer > ();

        listaDeJugadores.put( "Dairan", 1 );
        listaDeJugadores.put( "Dairan", 1 );
        listaDeJugadores.put( "Luis", 5 );

        for ( Map.Entry < String, Integer> entry: listaDeJugadores.entrySet() )
        {
            System.out.println("Key = " + entry.getKey() + " , Value = " + entry.getValue());
        }
    }
}
