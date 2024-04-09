import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
//import './App.css'

import UsuariosData from './mock-data/UsuariosData';


import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import Home from './components/Home/Home';
// ------------------- Imports Usuarios -------------------
import MostrarUsuarios from './components/Usuarios/MostrarUsuarios';
import EliminarRegistro from './components/Registros/EliminarRegistro';
import RegistrarUsuario from './components/Usuarios/RegistrarUsuario';
import PedirIdParaActualizar from './components/Registros/PedirIdParaActualizar';
import ActualizarUsuario from './components/Usuarios/ActualizarUsuario';

function App() {
  let usuarios = UsuariosData();
  const router = createBrowserRouter(createRoutesFromElements(
    <>
      <Route path='home' element={<Home />} />
      <Route path='usuarios' element={<MostrarUsuarios usuarios={usuarios.usuarioArr} />} />
      <Route path='pedir-id-eliminar-usuario' element={<EliminarRegistro registros={usuarios} texto={"Usuario"} />} />
      <Route path='crear-usuario' element={<RegistrarUsuario usuarios={usuarios} />} />
      <Route path='pedir-id-usuario' element={<PedirIdParaActualizar registrosArr={usuarios} texto={"Usuario"} />} />
      <Route path='actualizar-usuario/:idUsuario' element={<ActualizarUsuario usuarios={usuarios} />} />
    </>

  ));

  return (
    <RouterProvider router={router} />
  )
}

export default App
