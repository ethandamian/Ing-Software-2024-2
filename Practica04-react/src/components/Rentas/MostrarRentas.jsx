import styles from "../styles/registros.module.css";
import { Link } from "react-router-dom";

export default function MostrarRentas({ rentas }) {
    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Registros de <strong className="negritas">Rentas</strong></p>
            </div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th className={styles.columnTitle} scope="col">IdRenta</th>
                        <th className={styles.columnTitle} scope="col">IdUsuario</th>
                        <th className={styles.columnTitle} scope="col">IdPelicula</th>
                        <th className={styles.columnTitle} scope="col">Fecha De Renta</th>
                        <th className={styles.columnTitle} scope="col">Dias de Renta</th>
                        <th className={styles.columnTitle} scope="col">Estatus</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        rentas.map((renta) => (
                            <tr className="table-dark" key={renta.idRentar} >
                                <th scope="row">{renta.idRentar}</th>
                                <td>{renta.idUsuario}</td>
                                <td>{renta.idPelicula}</td>
                                <td>{renta.fecha_rentar}</td>
                                <td>{renta.dias_de_renta} dias restantes</td>
                                <td>{renta.estatus ? 'Entragada' : 'No Entregada'}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    );
}