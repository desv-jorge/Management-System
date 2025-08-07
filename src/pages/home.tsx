import { FaEdit, FaTrashAlt, FaPlus } from "react-icons/fa";
import Cookies from "js-cookie";

import Header from "../components/header";

const services = [
  {
    cliente: "Jorge N.",
    tipo: "Troca de tela",
    data: "08/05/2025",
    status: "Em andamento",
    statusColor: "text-yellow-400"
  },
  {
    cliente: "Maria C.",
    tipo: "Troca de bateria",
    data: "02/05/2025",
    status: "Finalizado",
    statusColor: "text-green-500"
  },
  {
    cliente: "Henrique P.",
    tipo: "Película para tela",
    data: "12/05/2025",
    status: "Aguardando peças",
    statusColor: "text-red-500"
  },
  {
    cliente: "Lenom F.",
    tipo: "Troca de câmera",
    data: "06/05/2025",
    status: "Finalizado",
    statusColor: "text-green-500"
  },
  {
    cliente: "Núbia M.",
    tipo: "Troca de microfone",
    data: "13/05/2025",
    status: "Não iniciado",
    statusColor: "text-gray-400"
  },
];

export default function Dashboard() {

  // const token = Cookies.get("jwt_token");

  // const response = await fetch("http://localhost:8000/protected", {
  //   headers: {
  //     Authorization: `Bearer ${token}`,
  //   },
  // });

  return (
    <div className="min-h-screen bg-gray-200 font-sans">
      {/* Navbar */}
      <Header/>

      {/* Conteúdo principal */}
      <main className="p-8">
        <h1 className="text-4xl font-bold mb-6">Dashboards</h1>

        <div className="bg-white rounded-xl p-6 shadow-md">
          <h2 className="text-2xl font-semibold mb-4">Painel de Serviços</h2>

          <div className="overflow-x-auto">
            <table className="min-w-full text-left border rounded-xl">
              <thead className="bg-gray-400 text-gray-900">
                <tr>
                  <th className="p-3">Cliente</th>
                  <th className="p-3">Tipo</th>
                  <th className="p-3">Data de solicitação</th>
                  <th className="p-3">Status</th>
                  <th className="p-3 text-center">Ações</th>
                </tr>
              </thead>
              <tbody className="bg-gray-100">
                {services.map((servico, index) => (
                  <tr key={index} className="border-t">
                    <td className="p-3">{servico.cliente}</td>
                    <td className="p-3">{servico.tipo}</td>
                    <td className="p-3">{servico.data}</td>
                    <td className={`p-3 font-semibold ${servico.statusColor}`}>
                      {servico.status}
                    </td>
                    <td className="p-3 flex gap-3 justify-center text-xl">
                      <FaEdit className="text-black cursor-pointer" />
                      <FaTrashAlt className="text-red-600 cursor-pointer" />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Botões */}
          <div className="mt-6 flex justify-between items-center">
            <button className="bg-blue-600 text-white text-lg font-semibold px-6 py-2 rounded-full flex items-center gap-2 hover:bg-blue-700">
              Cadastrar novos serviços <FaPlus />
            </button>
            <a href="#" className="text-blue-700 font-bold hover:underline">
              Ver todo o histórico
            </a>
          </div>
        </div>
      </main>
    </div>
  );
}
