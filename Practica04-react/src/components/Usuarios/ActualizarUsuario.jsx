import styles from "../styles/forms.module.css";
import Swal from "sweetalert2";
import { useEffect } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import { isNumber } from "../Hooks/Validators/isNumber";
import { isOnlyLetters } from "../Hooks/Validators/isOnlyLetters";
import { isPasswordValid } from "../Hooks/Validators/isPasswordValid";
import useInput from "../Hooks/useInput";

export default function ActualizarUsuario({ usuarios }) {
    const { idUsuario } = useParams();
    const navigate = useNavigate();

    const nombreInput = useInput('', { errorMsg: "Ingresa sólo letras, sin espacios ni carácteres especiales.", validator: isOnlyLetters });
    const apePatInput = useInput('', { errorMsg: "Ingresa sólo letras, sin espacios ni carácteres especiales.", validator: isOnlyLetters });
    const apeMatInput = useInput('', { errorMsg: "Ingresa sólo letras, sin espacios ni carácteres especiales.", validator: isOnlyLetters });
    const passwordInput = useInput('', { errorMsg: "Ingresa una contraseña válida, debe contener al menos 8 caracteres.", validator: isPasswordValid });
    const emailInput = useInput('', { errorMsg: "Ingresa un email válido." });
    const superUserInput = useInput(false, { errorMsg: "", isCheckbox: true });

    useEffect(() => {
        const usuario = obtenerUsuario();
        nombreInput.setValue(usuario.nombre);
        apePatInput.setValue(usuario.apPat);
        apeMatInput.setValue(usuario.apMat);
        passwordInput.setValue(usuario.password);
        emailInput.setValue(usuario.email);
        superUserInput.setValue(usuario.superUser === 1 ? true : false);
        borrarAnterior();



    }, [])

    const borrarAnterior = () => {
        usuarios.setUsuarios((prevUsuarios) => prevUsuarios.filter(usuario => usuario.idUsuario !== parseInt(idUsuario)));
    }

    const obtenerUsuario = () => {
        const usuario = usuarios.usuarioArr.find(usuario => usuario.idUsuario === parseInt(idUsuario));
        return usuario;
    }

    const hayErrorers = () => {
        return nombreInput.error || apePatInput.error || apeMatInput.error || passwordInput.error || emailInput.error;
    }

    const existeUsuario = () => {
        const usuarioEncontrado = usuarios.usuarioArr.find(usuario => usuario.email === emailInput.value);
        return usuarioEncontrado === undefined ? false : true;
    }


    const onSubmitHandler = (e) => {
        e.preventDefault();

        let title = 'Error al crear usuario';
        let text = 'Por favor, revise los campos marcados en rojo.';
        let icon = 'error';
        if (existeUsuario()) {
            title = 'Error al actualizar usuario';
            text = 'El email ingresado ya existe. Por favor, ingrese otro email.';
            icon = 'error';
        } else {
            if (!hayErrorers()) {
                title = 'Usuario actualizado';
                text = 'Redirigiendose a la página principal... ';
                icon = 'success';
                const nuevoUsuario = {
                    "idUsuario": parseInt(idUsuario),
                    "nombre": nombreInput.value,
                    "apPat": apePatInput.value,
                    "apMat": apeMatInput.value,
                    "password": passwordInput.value,
                    "email": emailInput.value,
                    "superUser": superUserInput.value ? 1 : 0
                };
                usuarios.setUsuarios((prevUsuarios) => [...prevUsuarios, nuevoUsuario]);


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
                <Link type="button" className={`btn ${styles.btn} ${styles.regresar}`} to="/pedir-id-usuario">Regresar</Link>
                <p className={styles.title}>Actualizar <strong className={styles.negritas}>Usuario</strong></p>
                <p className={styles.subtitle}>Porfavor, ingrese los datos solicitados</p>
            </div>
            <div className={styles.formContainer}>
                <form onSubmit={onSubmitHandler}>
                    <div className="mb-4">
                        <label for="nombre" className="form-label">Nombre</label>
                        <input type="text" className={`form-control ${styles.input} ${nombreInput.error ? styles.error : ''}`} id="nombre" required
                            placeholder="Ingrese su Nombre" onChange={nombreInput.onChange} value={nombreInput.value} />
                        {nombreInput.error && <small style={{ color: 'red' }}>{nombreInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label for="apellidoPat" className="form-label">Apellido Paterno</label>
                        <input type="text" className={`form-control ${styles.input} ${apePatInput.error ? styles.error : ''}`} id="apePat" required
                            placeholder="Ingrese su Apellido Paterno" onChange={apePatInput.onChange} value={apePatInput.value} />
                        {apePatInput.error && <small style={{ color: 'red' }}>{apePatInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label for="apellidoMat" className="form-label">Apellido Materno</label>
                        <input type="text" class={`form-control ${styles.input} ${apeMatInput.error ? styles.error : ''}`} id="apeMat" required
                            placeholder="Ingrese su Apellido Materno" onChange={apeMatInput.onChange} value={apeMatInput.value} />
                        {apeMatInput.error && <small style={{ color: 'red' }}>{apeMatInput.error}</small>}

                    </div>
                    <div className="mb-4">
                        <label for="password" className="form-label">Contraseña</label>
                        <input type="password" class={`form-control ${styles.input} ${passwordInput.error ? styles.error : ''}`} id="password"
                            required onChange={passwordInput.onChange} value={passwordInput.value} />
                        {passwordInput.error && <small style={{ color: 'red' }}>{passwordInput.error}</small>}
                    </div>
                    <div className="mb-4">
                        <label for="email" className="form-label">Email</label>
                        <input type="email" className={`form-control ${styles.input} ${emailInput.error ? styles.error : ''}`} id="email"
                            required placeholder="Ingrese su Email" onChange={emailInput.onChange} value={emailInput.value} />
                        {emailInput.error && <small style={{ color: 'red' }}>{emailInput.error}</small>}
                    </div>
                    <div className="mb-3 form-check">
                        <input type="checkbox" className="form-check-input" id="superUser" onChange={superUserInput.onChange} checked={superUserInput.value} />
                        <label className="form-check-label" for="superUser">Super Usuario</label>
                    </div>
                    <div className={styles.btnSubmitContainer}>

                        <button type="submit" className={`btn ${styles.btnSubmit} ${styles.btn}`}>Actualizar</button>
                    </div>
                </form>
            </div>

        </div>

    )

}