import styles from "../styles/forms.module.css";
import Swal from "sweetalert2";
import { Link } from "react-router-dom";
import { isOnlyLettersAndSpace } from "../Hooks/Validators/isOnlyLettersAndSpace";
import { isNumber } from "../Hooks/Validators/isNumber";

import useInput from "../Hooks/useInput";

export default function RegistrarPelicula({ peliculas }) {
    const nombreInput = useInput('', { errorMsg: "Ingresa sólo letras.", validator: isOnlyLettersAndSpace });
    const generoInput = useInput('', { errorMsg: "Ingresa sólo letras.", validator: isOnlyLettersAndSpace });
    const duracionInput = useInput('', { errorMsg: "Ingresa sólo números.", validator: isNumber });
    const inventarioInput = useInput('', { errorMsg: "Ingresa sólo números.", validator: isNumber });

    const onSubmitHandler = (e) => {
        e.preventDefault();
        let title = 'Error al crear pelicula';
        let text = 'Por favor, revise los campos marcados en rojo.';
        let icon = 'error';
        if (existePelicula()) {
            title = 'Error al crear pelicula';
            text = 'La película con este nombre ya existe. Por favor, ingrese otro nombre.';
            icon = 'error';

        } else {
            if (!hayErrores()) {
                title = 'Pelicula creada';
                text = 'La pelicula ha sido creada exitosamente.';
                icon = 'success';
                const nuevaPelicula = {
                    "idPelicula": obtenerUltimoId(),
                    "nombre": nombreInput.value.trim(),
                    "genero": generoInput.value.trim(),
                    "duracion": parseInt(duracionInput.value),
                    "inventario": parseInt(inventarioInput.value)
                }
                peliculas.setPeliculas((prevPeliculas) => [...prevPeliculas, nuevaPelicula]);
                nombreInput.setValue('');
                generoInput.setValue('');
                duracionInput.setValue('');
                inventarioInput.setValue('');
            }
        }
        Swal.fire({
            title: title,
            text: text,
            icon: icon
        });

    }

    const hayErrores = () => {
        return nombreInput.error || generoInput.error || duracionInput.error || inventarioInput.error;
    }

    const obtenerUltimoId = () => {
        const ids = peliculas.peliculaArr.map(pelicula => pelicula.idPelicula);
        return Math.max(...ids) + 1;
    }

    const existePelicula = () => {
        const peliculaEncontrada = peliculas.peliculaArr.find(pelicula => pelicula.nombre === nombreInput.value);
        return peliculaEncontrada === undefined ? false : true;
    }

    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Crear <strong className={styles.negritas}>Pelicula</strong></p>
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

                        <button type="submit" className={`btn ${styles.btnSubmit} ${styles.btn}`}>Crear</button>
                    </div>
                </form>
            </div>
        </div>
    )

}