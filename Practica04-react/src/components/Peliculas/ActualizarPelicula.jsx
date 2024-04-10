import styles from "../styles/forms.module.css";
import Swal from "sweetalert2";
import { useEffect } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import { isOnlyLettersAndSpace } from "../Hooks/Validators/isOnlyLettersAndSpace";
import { isNumber } from "../Hooks/Validators/isNumber";

import useInput from "../Hooks/useInput";

export default function ActualizarPelicula({ peliculas }) {
    const { idPelicula } = useParams();
    const navigate = useNavigate();

    const nombreInput = useInput('', { errorMsg: "Ingresa sólo letras.", validator: isOnlyLettersAndSpace });
    const generoInput = useInput('', { errorMsg: "Ingresa sólo letras.", validator: isOnlyLettersAndSpace });
    const duracionInput = useInput('', { errorMsg: "Ingresa sólo números.", validator: isNumber });
    const inventarioInput = useInput('', { errorMsg: "Ingresa sólo números.", validator: isNumber });

    useEffect(() => {
        const pelicula = obtenerPelicula();
        nombreInput.setValue(pelicula.nombre);
        generoInput.setValue(pelicula.genero);
        duracionInput.setValue(pelicula.duracion);
        inventarioInput.setValue(pelicula.inventario);
        borrarAnterior();


    }, []);

    const borrarAnterior = () => {
        peliculas.setPeliculas((prevPeliculas) => prevPeliculas.filter(pelicula => pelicula.idPelicula !== parseInt(idPelicula)));
    }

    const obtenerPelicula = () => {
        const pelicula = peliculas.peliculaArr.find(pelicula => pelicula.idPelicula === parseInt(idPelicula));
        return pelicula;
    }

    const hayErrores = () => {
        return nombreInput.error || generoInput.error || duracionInput.error || inventarioInput.error;
    }

    const existePelicula = () => {
        const peliculaEncontrada = peliculas.peliculaArr.find(pelicula => pelicula.nombre === nombreInput.value);
        return peliculaEncontrada === undefined ? false : true;
    }

    const onSubmitHandler = (e) => {
        e.preventDefault();
        let title = 'Error al crear pelicula';
        let text = 'Por favor, revise los campos marcados en rojo.';
        let icon = 'error';
        if (existePelicula()) {
            title = 'Error al actualizar pelicula';
            text = 'La película con este nombre ya existe. Por favor, ingrese otro nombre.';
            icon = 'error';

        } else {
            if (!hayErrores()) {
                title = 'Pelicula actualizada';
                text = 'Redirigiendose a la pagina principal... ';
                icon = 'success';
                const nuevaPelicula = {
                    "idPelicula": parseInt(idPelicula),
                    "nombre": nombreInput.value.trim(),
                    "genero": generoInput.value.trim(),
                    "duracion": parseInt(duracionInput.value),
                    "inventario": parseInt(inventarioInput.value)
                }
                peliculas.setPeliculas((prevPeliculas) => [...prevPeliculas, nuevaPelicula]);
                setTimeout(() => {

                    navigate(-2);

                }, 2000);
            }
        }
        Swal.fire({
            title: title,
            text: text,
            icon: icon
        });
    }

    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Menu Principal</Link>
                <Link type="button" className={`btn ${styles.btn} ${styles.regresar}`} to="/pedir-id-pelicula">Regresar</Link>
                <p className={styles.title}>Actualizar <strong className={styles.negritas}>Pelicula</strong></p>
                <p className={styles.subtitle}>Porfavor, ingrese los datos solicitados</p>
            </div>
            <div className={styles.formContainer}>
                <form onSubmit={onSubmitHandler}>
                    <div className="mb-4">
                        <label className="form-label">Nombre</label>
                        <input type="text" className={`form-control ${styles.input} ${nombreInput.error ? styles.error : ''}`} required
                            placeholder="Ingrese el Nombre de la Pelicula" onChange={nombreInput.onChange} value={nombreInput.value} />
                        {nombreInput.error && <small style={{ color: 'red' }}>{nombreInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label className="form-label">Género</label>
                        <input type="text" className={`form-control ${styles.input} ${generoInput.error ? styles.error : ''}`} required
                            placeholder="Ingrese el Genero" onChange={generoInput.onChange} value={generoInput.value} />
                        <div id="genero_help" className={styles.formText}>Escriba los generos separados por |</div>
                        {generoInput.error && <small style={{ color: 'red' }}>{generoInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label className="form-label">Duración</label>
                        <input type="text" className={`form-control ${styles.input} ${duracionInput.error ? styles.error : ''}`} id="duracionId" name="duracion" required
                            placeholder="Ingrese la duración de la pelicula" min="1" onChange={duracionInput.onChange} value={duracionInput.value} />
                        <div id="genero_help" className={styles.formText}>Debe ser escritos en minutos</div>
                        {duracionInput.error && <small style={{ color: 'red' }}>{duracionInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label className="form-label">Inventario</label>
                        <input type="text" className={`form-control ${styles.input} ${inventarioInput.error ? styles.error : ''}`} id="inventarioID" name="inventario" required min="1"
                            placeholder="Ingrese el numero en el inventario" onChange={inventarioInput.onChange} value={inventarioInput.value} />
                        {inventarioInput.error && <small style={{ color: 'red' }}>{inventarioInput.error}</small>}
                    </div>
                    <div className={styles.btnSubmitContainer}>

                        <button type="submit" className={`btn ${styles.btnSubmit} ${styles.btn}`}>Actualizar</button>
                    </div>
                </form>
            </div>
        </div>
    )
}