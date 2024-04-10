
import styles from '../styles/home.module.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'bootstrap';
import { Link } from "react-router-dom";

export default function Home() {

    return (
        <>
            <main className={styles.main}>
                <h1 className={styles.title}>Bienvenido a ClonBuster, elige una de las opciones debajo</h1>
                <div className={styles.cardContainer}>
                    <div className={`card text-bg-dark ${styles.card}`}>
                        <div className={styles.cardBody} >
                            <h2 className="card-title">Usuarios</h2>
                            <p className="card-text">CRUD para el Usuario.</p>
                            <button className={`btn btn-secondary dropdown-toggle ${styles.btn}`} type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                Seleccione una accion
                            </button>
                            <ul className="dropdown-menu dropdown-menu-dark">
                                <li><Link className="dropdown-item" to="/usuarios">Obtener todos los Usuarios</Link></li>
                                <li><Link className="dropdown-item" to="/crear-usuario"> Crear Usuario</Link></li>
                                <li><Link className="dropdown-item" to="/pedir-id-eliminar-usuario">Borrar Usuario</Link>
                                </li>
                                <li><Link className="dropdown-item" to="/pedir-id-usuario">Actualizar información de Usuario</Link></li>
                            </ul>


                        </div>
                    </div>
                    <div className={`card text-bg-dark ${styles.card}`}>
                        <div className={styles.cardBody}>
                            <h2 className="card-title">Peliculas</h2>
                            <p className="card-text">CRUD para las Peliculas.</p>
                            <button className={`btn btn-secondary dropdown-toggle ${styles.btn}`} type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                Seleccione una accion
                            </button>
                            <ul className="dropdown-menu dropdown-menu-dark">
                                <li><Link className="dropdown-item" to="/peliculas">Obtener todas las
                                    Peliculas</Link></li>
                                <li><Link className="dropdown-item" to="/crear-pelicula">Crear Pelicula</Link>
                                </li>
                                <li><Link className="dropdown-item" to="/pedir-id-eliminar-pelicula">Borrar Pelicula</Link>
                                </li>
                                <li><Link className="dropdown-item" to="/pedir-id-pelicula">Actualizar
                                    información de una Pelicula</Link></li>
                            </ul>
                        </div>
                    </div>
                    <div className={`card text-bg-dark ${styles.card}`}>
                        <div className={styles.cardBody}>
                            <h2 className="card-title">Rentas</h2>
                            <p className="card-text">CRU para las Rentas.</p>
                            <button className={`btn btn-secondary dropdown-toggle ${styles.btn}`} type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                Seleccione una accion
                            </button>
                            <ul className="dropdown-menu dropdown-menu-dark">
                                <li><Link className="dropdown-item" to="/rentas" >Obtener todas las Rentas</Link>
                                </li>
                                <li><Link className="dropdown-item" to="/crear-renta">Crear Renta</Link></li>
                                <li><Link className="dropdown-item" to="/pedir-id-renta" >Actualizar Renta</Link></li>
                            </ul>
                        </div>
                    </div>

                </div>
            </main >
        </>
    )
}