import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import Header from "../../components/header";

export default function ServiceRegister() {
  const [formData, setFormData] = useState({
    client: "",
    device: "",
    description: "",
    email: "",
  });

  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const token = Cookies.get("jwt_token");
    try {
      const response = await fetch("http://127.0.0.1:8000/register/services", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        alert("Serviço cadastrado com sucesso!");
        navigate("/dashboard");
      } else {
        alert("Erro ao cadastrar serviço.");
      }
    } catch (error) {
      alert("Erro na requisição.");
      console.error(error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-200 font-sans flex flex-col">
      {/* Header fixo */}
      <Header />

      {/* Conteúdo centralizado */}
      <main className="flex flex-1 items-center justify-center px-4 py-8">
        <div className="w-full max-w-2xl bg-white rounded-xl shadow-md p-6 sm:p-8">
          <h2 className="text-xl sm:text-2xl font-semibold mb-6 text-center">
            Cadastrar novo serviço
          </h2>

          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <label className="flex flex-col text-sm sm:text-base">
              Cliente
              <input
                type="text"
                name="client"
                value={formData.client}
                onChange={handleChange}
                className="border rounded px-3 py-2"
                required
              />
            </label>

            <label className="flex flex-col text-sm sm:text-base">
              Aparelho
              <input
                type="text"
                name="device"
                value={formData.device}
                onChange={handleChange}
                className="border rounded px-3 py-2"
                required
              />
            </label>

            <label className="flex flex-col text-sm sm:text-base">
              Descrição
              <textarea
                name="description"
                value={formData.description}
                onChange={handleChange}
                className="border rounded px-3 py-2 resize-none"
                rows={4}
                required
              />
            </label>

            <label className="flex flex-col text-sm sm:text-base">
              Email
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="border rounded px-3 py-2"
                required
              />
            </label>

            <div className="flex flex-col sm:flex-row justify-between gap-4 mt-6">
              <button
                type="button"
                onClick={() => navigate("/dashboard")}
                className="w-full sm:w-auto px-6 py-2 border rounded hover:bg-gray-100 cursor-pointer"
              >
                Voltar
              </button>

              <button
                type="submit"
                className="w-full sm:w-auto px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 cursor-pointer"
              >
                Cadastrar
              </button>
            </div>
          </form>
        </div>
      </main>
    </div>
  );
}
