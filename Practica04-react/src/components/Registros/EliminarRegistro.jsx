import { useState } from "react";
import { Link } from "react-router-dom";
import Swal from 'sweetalert2';
import styles from '../styles/forms.module.css';
import useInput from "../Hooks/useInput";
import { isNumber } from "../Hooks/Validators/isNumber";

export default function EliminarRegistro({ registros, texto }) {

    const idInput = useInput("", { errorMsg: "Ingresa sólo números.", validator: isNumber });


    const onSubmitHandler = (e) => {
        e.preventDefault();

        Swal.fire({
            title: "¿Estás seguro de eliminar este registro?",
            text: "Esta acción es irreversible!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#564bc0",
            cancelButtonColor: "#d33",
            confirmButtonText: "Si, elimínalo",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {
                let title = '';
                let text = '';
                let icon = '';
                if (!eliminarRegistro()) {
                    title = "Error";
                    text = `El ${texto.toLowerCase()} no existe o ingresó un id incorrecto. Por favor, intente de nuevo.`;
                    icon = "error";

                } else {
                    title = "Eliminado";
                    text = `El registro ${texto == 'Usuario' ? 'del' : 'de la'} ${texto.toLowerCase()} ha sido eliminado exitosamente.`;
                    icon = "success";

                }
                Swal.fire({
                    title: title,
                    text: text,
                    icon: icon,
                });
                idInput.setValue('');
                idInput.setError('');

            }
        });

    }

    const existeRegistro = () => {
        const registroEncontrado = registros[`${texto.toLowerCase()}Arr`].find(registro => registro[`id${texto}`] === parseInt(idInput.value));
        return registroEncontrado === undefined ? false : true;
    }

    const eliminarRegistro = () => {
        if (!existeRegistro()) {
            return false;
        } else {
            registros[`set${texto}s`]((reg) => reg.filter(registro => registro[`id${texto}`] !== parseInt(idInput.value)));
            return true;
        }
    }
    return (
        <div className={styles.mainContainer}>
            <div className="header">
                <Link type="button" className={`btn ${styles.btn}`} to="/home">Regresar</Link>
                <p className={styles.title}>Eliminar<strong className={styles.negritas}>{texto}</strong></p>
                <p className={styles.subtitle}>Porfavor, ingrese el id {texto === 'Usuario' ? 'del' : 'de la'} {texto.toLowerCase()} a eliminar</p>

            </div>
            <div className={styles.formContainer}>
                <form onSubmit={onSubmitHandler}>
                    <div className="mb-4">
                        <label className="form-label">Id {texto}</label>
                        <input type="text" className={`form-control ${styles.input} ${idInput.error ? styles.error : ''}`} name="idInput" required value={idInput.value}
                            onChange={idInput.onChange}
                            placeholder={`id ${texto === 'Usuario' ? 'del' : 'de la'} ${texto.toLowerCase()} a eliminar`} min="1" />
                        {idInput.error && <small style={{ color: 'red' }}>{idInput.error}</small>}

                    </div>
                    <div className={styles.btnSubmitContainer}>

                        <button type="submit" className={`btn ${styles.btnSubmit} ${styles.btn}`}>Eliminar</button>
                    </div>
                </form>
            </div>
        </div>

    )
}