
import styles from "../styles/registros.module.css";
import { Link } from "react-router-dom";

export default function MostrarUsuarios({ usuarios }) {

    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Registros de <strong className="negritas">Usuarios</strong></p>
            </div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th className={styles.columnTitle} scope="col">Id</th>
                        <th className={styles.columnTitle} scope="col">Nombre</th>
                        <th className={styles.columnTitle} scope="col">Apellido Paterno</th>
                        <th className={styles.columnTitle} scope="col">Apellido Materno</th>
                        <th className={styles.columnTitle} scope="col">Email</th>
                        <th className={styles.columnTitle} scope="col">SuperUser</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        usuarios.map((usuario) => (
                            <tr className="table-dark" key={usuario.idUsuario}>
                                <th scope="row">{usuario.idUsuario}</th>
                                <td>{usuario.nombre}</td>
                                <td>{usuario.apPat}</td>
                                <td>{usuario.apMat}</td>
                                <td>{usuario.email}</td>
                                <td>{usuario.superUser ? 'Si' : 'No'}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    )

}