import { RiAccountCircleFill } from "react-icons/ri";
import logo from "../assets/logo.jpg";

export default function Header(){
    return(
        <header className="bg-black text-white flex justify-between items-center px-6 py-4">
        <div className="flex items-center gap-2">
          <img src={logo} alt="+ Celulares" className="size-12 rounded-full" />
        </div>
        <nav className="flex gap-8 text-lg">
          <a href="#" className="underline">Início</a>
          <a href="#">Estoque</a>
          <a href="#">Serviços</a>
          <a href="#">Clientes</a>
          <a href="#">Vendas</a>
        </nav>
        <div className="text-2xl">
            <RiAccountCircleFill className="size-12"/>
        </div>
      </header>
    )
}