import { useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
//import './App.css'

import UsuariosData from './mock-data/UsuariosData';
import PeliculasData from './mock-data/PeliculasData';
import RentasData from './mock-data/RentasData';


import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import Home from './components/Home/Home';
// ------------------- Imports componentes para los tres objetos -------------------
import PedirIdParaActualizar from './components/Registros/PedirIdParaActualizar';
import EliminarRegistro from './components/Registros/EliminarRegistro';
// ------------------- Imports Usuarios -------------------
import MostrarUsuarios from './components/Usuarios/MostrarUsuarios';
import RegistrarUsuario from './components/Usuarios/RegistrarUsuario';
import ActualizarUsuario from './components/Usuarios/ActualizarUsuario';

// ------------------- Imports Peliculas -------------------
import MostrarPeliculas from './components/Peliculas/MostrarPeliculas';
import RegistrarPelicula from './components/Peliculas/RegistrarPelicula';
import ActualizarPelicula from './components/Peliculas/ActualizarPelicula';


// ------------------- Imports Rentas -------------------
import MostrarRentas from './components/Rentas/MostrarRentas';
import RegistrarRenta from './components/Rentas/RegistrarRenta';
import ActualizarRenta from './components/Rentas/ActualizarRenta';


function App() {
  // Initialize data
  const usuarios = UsuariosData();
  const peliculas = PeliculasData();
  const rentas = RentasData();

  const router = createBrowserRouter(createRoutesFromElements(
    <>
      <Route path='home' element={<Home />} />
      // ------------------- Usuarios -------------------
      <Route path='usuarios' element={<MostrarUsuarios usuarios={usuarios.usuarioArr} />} />
      <Route path='pedir-id-eliminar-usuario' element={<EliminarRegistro registros={usuarios} texto={"Usuario"} />} />
      <Route path='crear-usuario' element={<RegistrarUsuario usuarios={usuarios} />} />
      <Route path='pedir-id-usuario' element={<PedirIdParaActualizar registrosArr={usuarios} texto={"Usuario"} />} />
      <Route path='actualizar-usuario/:idUsuario' element={<ActualizarUsuario usuarios={usuarios} />} />

      // ------------------- Peliculas -------------------
      <Route path='peliculas' element={<MostrarPeliculas peliculas={peliculas.peliculaArr} />} />
      <Route path='crear-pelicula' element={<RegistrarPelicula peliculas={peliculas} />} />
      <Route path='pedir-id-eliminar-pelicula' element={<EliminarRegistro registros={peliculas} texto={"Pelicula"} />} />
      <Route path='pedir-id-pelicula' element={<PedirIdParaActualizar registrosArr={peliculas} texto={"Pelicula"} />} />
      <Route path='actualizar-pelicula/:idPelicula' element={<ActualizarPelicula peliculas={peliculas} />} />

    // ------------------- Rentas -------------------
      <Route path='rentas' element={<MostrarRentas rentas={rentas.rentaArr} />} />
      <Route path='crear-renta' element={<RegistrarRenta rentas={rentas} />} />
      <Route path='pedir-id-renta' element={<PedirIdParaActualizar registrosArr={rentas} texto={"Renta"} />} />
      <Route path='actualizar-renta/:idRenta' element={<ActualizarRenta rentas={rentas} />} />
    </>

  ));

  return (
    <RouterProvider router={router} />
  )
}

export default App
