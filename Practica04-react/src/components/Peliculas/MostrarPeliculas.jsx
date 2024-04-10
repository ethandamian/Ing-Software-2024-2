import styles from "../styles/registros.module.css";
import { Link } from "react-router-dom";

export default function MostrarPeliculas({ peliculas }) {
    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Registros de <strong className="negritas">Peliculas</strong></p>
            </div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th className={styles.columnTitle} scope="col">IdPelicula</th>
                        <th className={styles.columnTitle} scope="col">Nombre</th>
                        <th className={styles.columnTitle} scope="col">Genero</th>
                        <th className={styles.columnTitle} scope="col">Duracion</th>
                        <th className={styles.columnTitle} scope="col">Inventario</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        peliculas.map((pelicula) => (
                            <tr className="table-dark" key={pelicula.idPelicula}>
                                <th scope="row">{pelicula.idPelicula}</th>
                                <td>{pelicula.nombre}</td>
                                <td>{pelicula.genero}</td>
                                <td>{pelicula.duracion}min</td>
                                <td>{pelicula.inventario} en stock</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    )
}