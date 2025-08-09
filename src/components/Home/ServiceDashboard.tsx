import { FaEdit, FaTrashAlt, FaPlus, FaInfoCircle } from "react-icons/fa";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import PopupConfirm from "../popUps/ConfirmDelete";
import PopupServiceInfo from "../popUps/serviceInfo"; // importar novo componente

export default function ServiceDashboard() {
  const [services, setServices] = useState<any[]>([]);
  const [showPopup, setShowPopup] = useState(false);
  const [idToDelete, setIdToDelete] = useState<number | null>(null);
  const [selectedService, setSelectedService] = useState<any | null>(null);

  const navigate = useNavigate();

  const goToCadastro = () => {
    navigate("/service-register");
  };

  useEffect(() => {
    const fetchServices = async () => {
      const token = Cookies.get("jwt_token");
      try {
        const response = await fetch("http://127.0.0.1:8000/get/services", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        const servicesJson = await response.json();
        const servicesArray = Array.isArray(servicesJson) ? servicesJson : [];
        setServices(servicesArray);
      } catch (error) {
        console.error("Erro ao buscar serviços:", error);
      }
    };

    fetchServices();
  }, []);

  const deleteService = async (id: number) => {
    try {
      const token = Cookies.get("jwt_token");
      const response = await fetch(`http://127.0.0.1:8000/delete/service/${id}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (response.ok) {
        setServices((prev) => prev.filter((s) => s.id !== id));
      } else {
        console.error("Erro ao deletar serviço:", response.status);
      }
    } catch (error) {
      console.error("Erro na requisição:", error);
    }
  };

  const askDelete = (id: number) => {
    setIdToDelete(id);
    setShowPopup(true);
  };

  const confirmDelete = () => {
    if (idToDelete !== null) {
      deleteService(idToDelete);
      setShowPopup(false);
      setIdToDelete(null);
    }
  };

  const cancelDelete = () => {
    setShowPopup(false);
    setIdToDelete(null);
  };

    const showServiceInfo = (service: any) => {
    setSelectedService(service);
  };

  return (
    <div className="bg-white rounded-xl p-4 sm:p-6 shadow-md">
      <h2 className="text-xl sm:text-2xl font-semibold mb-4">Painel de Serviços</h2>

      {/* Tabela responsiva */}
      <div className="overflow-x-auto">
        <table className="min-w-full text-left border rounded-xl text-sm sm:text-base">
          <thead className="bg-gray-400 text-gray-900">
            <tr>
              <th className="p-3">Cliente</th>
              <th className="p-3">Aparelho</th>
              <th className="p-3 whitespace-nowrap">Momento da solicitação</th>
              <th className="p-3 text-center">Ações</th>
            </tr>
          </thead>
          <tbody className="bg-gray-100">
            {services.slice(0, 5).map((servico, index) => (
              <tr key={index} className="border-t hover:bg-gray-200">
                <td className="p-3">{servico.client}</td>
                <td className="p-3">{servico.device}</td>
                <td className="p-3 whitespace-nowrap">{servico.created_at}</td>
                <td className="p-3 flex flex-wrap gap-3 justify-center text-lg sm:text-xl">
                  <FaEdit className="text-black cursor-pointer" />
                  <FaInfoCircle onClick={() => showServiceInfo(servico)} className="text-black cursor-pointer" />
                  <FaTrashAlt
                    onClick={() => askDelete(servico.id)}
                    className="text-red-600 cursor-pointer"
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Botões */}
      <div className="mt-6 flex flex-col sm:flex-row gap-4 sm:justify-between sm:items-center">
        <button
          onClick={goToCadastro}
          className="bg-blue-600 text-white text-sm sm:text-lg font-semibold px-4 sm:px-6 py-2 rounded-full flex items-center justify-center gap-2 hover:bg-blue-700 cursor-pointer"
        >
          Cadastrar novos serviços <FaPlus />
        </button>
        <a
          href="#"
          className="text-blue-700 font-bold text-sm sm:text-base hover:underline text-center sm:text-left"
        >
          Ver todo o histórico
        </a>
      </div>

      {showPopup && (
        <PopupConfirm
          message="Você realmente deseja excluir? O objeto será deletado permanentemente."
          onConfirm={confirmDelete}
          onCancel={cancelDelete}
        />
      )}
      
      {selectedService && (
        <PopupServiceInfo
          service={selectedService}
          onClose={() => setSelectedService(null)}
        />
      )}
    </div>
  );
}
