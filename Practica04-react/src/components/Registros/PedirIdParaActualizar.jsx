
import { Link, useNavigate } from "react-router-dom";
import Swal from 'sweetalert2';
import styles from '../styles/forms.module.css';
import useInput from "../Hooks/useInput";
import { isNumber } from "../Hooks/Validators/isNumber";

export default function PedirIdParaActualizar({ registrosArr, texto }) {
    const idInput = useInput("", { errorMsg: "Ingresa sólo números.", validator: isNumber });
    const navigate = useNavigate();

    const existeRegistro = () => {
        const registroEncontrado = registrosArr[`${texto.toLowerCase()}Arr`].find(registro => registro[texto === 'Renta' ? `id${texto}r` : `id${texto}`] === parseInt(idInput.value));
        return registroEncontrado === undefined ? false : true;
    }

    const onSubmitHandler = (e) => {
        e.preventDefault();
        if (existeRegistro()) {
            navigate(`/actualizar-${texto.toLowerCase()}/${idInput.value}`);

        } else {
            Swal.fire({
                title: "Error",
                text: `El ${texto.toLowerCase()} no existe o ingresó un id incorrecto. Por favor, intente de nuevo.`,
                icon: "error"
            });

        }

    }

    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Solicitar id <strong className={styles.negritas}>{texto}</strong></p>
                <p className={styles.subtitle}>Porfavor, ingrese el id {texto === 'Usuario' ? 'del' : 'de la'} {texto.toLowerCase()} a buscar</p>

            </div>
            <div className={styles.formContainer}>
                <form onSubmit={onSubmitHandler}>
                    <div className="mb-4">
                        <label className="form-label">Id {texto}</label>
                        <input type="text" className={`form-control ${styles.input} ${idInput.error ? styles.error : ''}`} name="idInput" required value={idInput.value}
                            onChange={idInput.onChange}
                            placeholder={`id ${texto === 'Usuario' ? 'del' : 'de la'} ${texto.toLowerCase()} a buscar`} min="1" />
                        {idInput.error && <small style={{ color: 'red' }}>{idInput.error}</small>}

                    </div>
                    <div className={styles.btnSubmitContainer}>

                        <button type="submit" className={`btn ${styles.btnSubmit} ${styles.btn}`}>Buscar</button>
                    </div>
                </form>
            </div>
        </div>

    )


}