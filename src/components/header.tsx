import { RiAccountCircleFill } from "react-icons/ri";
import { FaBars, FaTimes } from "react-icons/fa";
import logo from "../assets/logo.jpg";
import { useState } from "react";

export default function Header() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header className="bg-black text-white flex justify-between items-center px-6 py-4 relative">
      {/* Logo */}
      <div className="flex items-center gap-2">
        <img src={logo} alt="+ Celulares" className="size-12 rounded-full" />
      </div>

      {/* Menu Desktop */}
      <nav className="hidden md:flex gap-8 text-lg">
        <a href="#">Início</a>
        <a href="#">Estoque</a>
        <a href="#">Serviços</a>
        <a href="#">Clientes</a>
        <a href="#">Vendas</a>
      </nav>

      {/* Ícone de conta */}
      <div className="hidden md:block text-2xl">
        <RiAccountCircleFill className="size-12" />
      </div>

      {/* Botão Menu Mobile */}
      <button
        className="md:hidden text-2xl"
        onClick={() => setMenuOpen(!menuOpen)}
      >
        {menuOpen ? <FaTimes /> : <FaBars />}
      </button>

      {/* Menu Mobile */}
      {menuOpen && (
        <div className="absolute top-full left-0 w-full bg-black flex flex-col items-center gap-6 py-6 md:hidden z-50">
          <a href="#" onClick={() => setMenuOpen(false)}>Início</a>
          <a href="#" onClick={() => setMenuOpen(false)}>Estoque</a>
          <a href="#" onClick={() => setMenuOpen(false)}>Serviços</a>
          <a href="#" onClick={() => setMenuOpen(false)}>Clientes</a>
          <a href="#" onClick={() => setMenuOpen(false)}>Vendas</a>
          <RiAccountCircleFill className="size-12" />
        </div>
      )}
    </header>
  );
}
