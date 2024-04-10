import styles from "../styles/forms.module.css";
import Swal from "sweetalert2";
import { Link } from "react-router-dom";
import { isOnlyLetters } from "../Hooks/Validators/isOnlyLetters";
import { isNumber } from "../Hooks/Validators/isNumber";
import useInput from "../Hooks/useInput";

export default function RegistrarRenta({ rentas }) {
    const idUsuarioInput = useInput('', { errorMsg: "Ingresa un id de usuario válido.", validator: isNumber });
    const idPeliculaInput = useInput('', { errorMsg: "Ingresa un id de película válido.", validator: isNumber });
    const fechaRentaInput = useInput('', { errorMsg: "Ingresa una fecha válida." });
    const diasRentaInput = useInput('', { errorMsg: "Ingresa un número válido.", validator: isNumber });
    const estatusInput = useInput('', { errorMsg: "Ingresa un estatus válido." });

    const hayErrorers = () => {
        return idUsuarioInput.error || idPeliculaInput.error || fechaRentaInput.error || diasRentaInput.error || estatusInput.error;
    }

    const obtenerUltimoId = () => {
        const ids = rentas.rentaArr.map(renta => renta.idRentar);
        return Math.max(...ids) + 1;
    }

    const existeRenta = () => {
        const rentaEncontrada = rentas.rentaArr.find(renta => (renta.idUsuario === idUsuarioInput.value && renta.idPelicula === idPeliculaInput.value));
        return rentaEncontrada === undefined ? false : true;
    }


    const onSubmitHandler = (e) => {
        let title = 'Error al crear renta';
        let text = 'Por favor, revise los campos marcados en rojo.';
        let icon = 'error';
        e.preventDefault();
        if (existeRenta()) {
            title = 'Error al crear renta';
            text = 'El usuario ya tiene rentada esta película.';
            icon = 'error';
        } else {
            if (!hayErrorers()) {
                title = 'Renta creada';
                text = 'La renta ha sido creada exitosamente.';
                icon = 'success';;
                const nuevaRenta = {
                    "idRentar": obtenerUltimoId(),
                    "idUsuario": parseInt(idUsuarioInput.value),
                    "idPelicula": parseInt(idPeliculaInput.value),
                    "fecha_rentar": fechaRentaInput.value,
                    "dias_de_renta": diasRentaInput.value ? parseInt(diasRentaInput.value) : 5,
                    "estatus": estatusInput.value ? 1 : 0
                };

                rentas.setRentas((prevRentas) => [...prevRentas, nuevaRenta]);
                idUsuarioInput.setValue('');
                idPeliculaInput.setValue('');
                fechaRentaInput.setValue('');
                diasRentaInput.setValue('');
                estatusInput.setValue('');
            }
        }
        Swal.fire({
            title: title,
            text: text,
            icon: icon,
        });


    }

    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Crear <strong className={styles.negritas}>Renta</strong></p>
                <p className={styles.subtitle}>Porfavor, ingrese los datos solicitados</p>
            </div>
            <div className={styles.formContainer}>
                <form onSubmit={onSubmitHandler}>
                    <div className="mb-4">
                        <label className="form-label">Id Usuario</label>
                        <input type="text" class="form-control" required
                            placeholder="Ingrese el id del usuario" min="1" onChange={idUsuarioInput.onChange} value={idUsuarioInput.value} />
                        {idUsuarioInput.error && <small style={{ color: 'red' }}>{idUsuarioInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label className="form-label">Id Pelicula</label>
                        <input type="text" className="form-control" required
                            placeholder="Ingrese el id de la pelicula" min="1" onChange={idPeliculaInput.onChange} value={idPeliculaInput.value} />
                        {idPeliculaInput.error && <small style={{ color: 'red' }}>{idPeliculaInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label className="form-label">Fecha de Renta</label>
                        <input type="date" className="form-control" required
                            placeholder="Ingrese la fecha de renta" onChange={fechaRentaInput.onChange} value={fechaRentaInput.value} />
                        {fechaRentaInput.error && <small style={{ color: 'red' }}>{fechaRentaInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label className="form-label">Dias de Renta</label>
                        <input type="text" className="form-control" min="0"
                            placeholder="Ingrese los dias de renta" onChange={diasRentaInput.onChange} value={diasRentaInput.value} />
                        {diasRentaInput.error && <small style={{ color: 'red' }}>{diasRentaInput.error}</small>}
                        <div id="dias_renta_help" className={styles.formText}>Si no rellena este campo, automaticamente se pondran 5 dias
                            de renta</div>
                    </div>
                    <div className="mb-3 form-check">
                        <label className="form-check-label">Entregada</label>
                        <input type="checkbox" className="form-check-input" onChange={estatusInput.onChange} value={estatusInput.value} />
                        {estatusInput.error && <small style={{ color: 'red' }}>{estatusInput.error}</small>}

                    </div>
                    <div className={styles.btnSubmitContainer}>

                        <button type="submit" className={`btn ${styles.btnSubmit} ${styles.btn}`}>Crear</button>
                    </div>
                </form>
            </div>
        </div>
    );


}