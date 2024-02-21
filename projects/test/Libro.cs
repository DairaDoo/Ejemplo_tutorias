class Libro
{
        private string bookName;
        private int releaseYear;


        public Libro(string name, int year)
        {
            bookName = name;
                releaseYear = year;
        }

        public void setBookName( string name )
        {
            bookName = name;
        }

        public void setReleaseYear( int year )
        {
            releaseYear = year;
        }

        public string getBookName()
        {
            return bookName;
        }

        public int getSetRelease()
        {
            return releaseYear;
        }

        public String info()
        {
            return "Nombre Libro: " + bookName + "| Año de salida: " + releaseYear;
        }
    }