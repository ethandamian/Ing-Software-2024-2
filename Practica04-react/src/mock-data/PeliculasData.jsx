import { useState } from "react"

export default function PeliculasData() {
    const [peliculaArr, setPeliculas] = useState([{
        "idPelicula": 1,
        "nombre": "Descendant of the Sun (Ri jie)",
        "genero": "Action|Adventure|Fantasy|Sci-Fi",
        "duracion": 128,
        "inventario": 8
    }, {
        "idPelicula": 2,
        "nombre": "Jacques Brel Is Alive and Well and Living in Paris",
        "genero": "Musical",
        "duracion": 134,
        "inventario": 10
    }, {
        "idPelicula": 3,
        "nombre": "Spin (You Are Here)",
        "genero": "Comedy|Romance",
        "duracion": 97,
        "inventario": 1
    }, {
        "idPelicula": 4,
        "nombre": "Wings of Honneamise (Ôritsu uchûgun Oneamisu no tsubasa)",
        "genero": "Animation|Drama|Sci-Fi|War",
        "duracion": 68,
        "inventario": 2
    }, {
        "idPelicula": 5,
        "nombre": "Dead Next Door, The",
        "genero": "Horror",
        "duracion": 71,
        "inventario": 17
    }, {
        "idPelicula": 6,
        "nombre": "The Sinners of Hell",
        "genero": "Drama|Horror",
        "duracion": 171,
        "inventario": 18
    }, {
        "idPelicula": 7,
        "nombre": "Igor",
        "genero": "Animation|Comedy",
        "duracion": 140,
        "inventario": 14
    }, {
        "idPelicula": 8,
        "nombre": "Love and Lemons (Små citroner gula)",
        "genero": "Romance",
        "duracion": 93,
        "inventario": 11
    }, {
        "idPelicula": 9,
        "nombre": "Funeral, The (Ososhiki)",
        "genero": "Comedy",
        "duracion": 118,
        "inventario": 13
    }, {
        "idPelicula": 10,
        "nombre": "Hard Man, The",
        "genero": "Western",
        "duracion": 153,
        "inventario": 3
    }, {
        "idPelicula": 11,
        "nombre": "Subject Two",
        "genero": "Drama|Thriller",
        "duracion": 98,
        "inventario": 19
    }, {
        "idPelicula": 12,
        "nombre": "Dead Girl, The",
        "genero": "Drama|Mystery|Thriller",
        "duracion": 130,
        "inventario": 13
    }, {
        "idPelicula": 13,
        "nombre": "Guide, The (O Xenagos)",
        "genero": "Drama",
        "duracion": 66,
        "inventario": 15
    }, {
        "idPelicula": 14,
        "nombre": "Americanization of Emily, The",
        "genero": "Comedy|Drama|War",
        "duracion": 85,
        "inventario": 6
    }, {
        "idPelicula": 15,
        "nombre": "Ghostbusters II",
        "genero": "Comedy|Fantasy|Sci-Fi",
        "duracion": 69,
        "inventario": 13
    }]);

    return { peliculaArr, setPeliculas };
}