using System;

namespace test
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Libro miLibro = new Libro("Juan", 2020); // creamos una instancia de la clase Libro.

            // miLibro.setBookName("Juan");

            
            // miLibro.setReleaseYear(2020);
            string res = miLibro.info();
            Console.WriteLine("Info: " + res);
        }
    }
}
