import logo from "../assets/logo.jpg";
import background from "../assets/celular.jpg";
import "../style.css";

function Login() {
  return (
    <div className="flex h-screen w-screen">
      {/* Lado esquerdo */}
      <div className="w-full sm:w-1/2 flex flex-col items-center justify-center bg-black text-white p-6">
        <img src={logo} alt="Logo + Celulares" className="w-52 mb-8" />

        <form className="w-72 flex flex-col gap-4">
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
              className="px-4 py-2 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <button
            type="submit"
            className="px-4 py-3 rounded bg-white text-gray-800 font-bold hover:bg-gray-300 transition-colors"
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
