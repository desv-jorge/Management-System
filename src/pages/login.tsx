import logo from "../assets/logo.jpg";
import background from "../assets/celular.jpg";
import { useState, type ChangeEvent, type FormEvent } from "react";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";

interface LoginFormValues {
  email: string;
  senha: string;
}

function Login() {
  const [values, setValues] = useState<LoginFormValues>({ email: "", senha: "" });
  const navigate = useNavigate();

  const onChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setValues((prevValues) => ({
      ...prevValues,
      [name]: value,
    }));
  };

const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
  event.preventDefault();

  try {
    const response = await fetch("http://localhost:8000/auth/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: values.email,
        password: values.senha,
      }),
    });

    if (!response.ok) {
      throw new Error("Erro ao autenticar. Verifique suas credenciais.");
    }

    const data = await response.json();

    const token = data.acess_token;

    Cookies.set("jwt_token", token, {
      secure: true,
      sameSite: "strict",
      expires: 1,
    });

    console.log("Token armazenado com sucesso.");

    // 🔥 Redireciona para o dashboard
    navigate("/dashboard");
  } catch (error) {
    console.error("Erro ao fazer login:", error);
  }
};



  return (
    <div className="flex h-screen w-screen">
      {/* Lado esquerdo */}
      <div className="w-full sm:w-1/2 flex flex-col items-center justify-center bg-black text-white p-6">
        <img src={logo} alt="Logo + Celulares" className="w-52 mb-8" />

        <form className="w-72 flex flex-col gap-4" onSubmit={handleSubmit}>
          <div className="flex flex-col">
            <label htmlFor="email" className="sr-only">
              Email
            </label>
            <input
              id="email"
              type="email"
              name="email"
              placeholder="Email"
              required
              value={values.email}
              onChange={onChange}
              className="px-4 py-2 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="senha" className="sr-only">
              Senha
            </label>
            <input
              id="senha"
              type="password"
              name="senha"
              placeholder="Senha"
              required
              value={values.senha}
              onChange={onChange}
              className="px-4 py-2 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <button
            type="submit"
            className="px-4 py-3 rounded bg-white text-gray-800 font-bold hover:bg-gray-300 transition-colors cursor-pointer"
          >
            ENTRAR
          </button>

          <a href="#" className="text-center text-sm text-gray-400 hover:underline">
            Esqueceu a senha?
          </a>
        </form>
      </div>

      {/* Lado direito (imagem) */}
      <div className="hidden sm:block w-1/2">
        <img
          src={background}
          alt="Imagem Login"
          className="w-full h-full object-cover"
        />
      </div>
    </div>
  );
}

export default Login;
